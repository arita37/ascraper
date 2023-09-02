"""
Works with GGUF models (GGML models are deprecated)

# GPU llama-cpp-python
    pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir --verbose
# For models download. Ignore if gguf is already downloaded
    pip install huggingface_hub
# Dependencies:
    pip install utilmy fire openai langchain
"""

from huggingface_hub import hf_hub_download
import ast, csv, fire
from utilmy import config_load, log

from llama_cpp import Llama
from langchain.prompts import PromptTemplate, FewShotPromptTemplate


################################################################################

def generate_kgraph(prompt=None, prompt_name='prompt1', dirout="kg_out.csv", cfg='llama_config.yml'):
    """
      Extrapolates the relationships from the given prompt.
      Uses a fewshot prompt template, specified in the config file.
    """
    config = config_load(cfg)

    prompt1 = prompt if isinstance(prompt, str) else config[prompt_name]

    #### Load specific config ##################################################
    cfg = config

    msetup = cfg['model_setup']
    repo_id = msetup['repo_id']
    model_basename = msetup['model_basename']
    model_path = hf_hub_download(repo_id=repo_id, filename=model_basename, local_dir='./models')

    mpars = cfg['model_params']
    prompt_params = cfg["prompt_params"]
    prompt_template_params = cfg['prompt_template']
    example_template_params = cfg['prompt_template_example']

    #### Example and Main templates ############################################
    example_prompt = PromptTemplate(**example_template_params)
    prompt_template = FewShotPromptTemplate(
        **prompt_template_params,
        example_prompt=example_prompt,
    )

    #### Model init and run ####################################################
    log(f"### Initializing model {msetup['model_basename']}")
    try:
        llm = Llama(
            model_path=model_path,
            **mpars
        )
        log(f'### Model successfuly initialized')
    except Exception as e:
        log(f'### Error while initializing model: {e}')
        return

    log(f"### Running the model...")
    _input = prompt_template.format(input=prompt1)
    response = llm(
        prompt=_input,
        **prompt_params
    )
    #### Parsing the response ##################################################
    reponse_text = response['choices'][0]['text']
    print(reponse_text)
    # log("### Parsing response")
    # try:
    #     output = ast.literal_eval(response['choices'][0])
    #     csv_write(output, dirout)
    #     log(f"Output written to {dirout}")
    # except Exception as e:
    #     log(f"Error editing the output: {e}")


################################################################################

##### utils ####################################################################
def csv_write(relations, dirout):
    with open(dirout, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['a', 'b', 'relation'])
        writer.writerows(relations)


################################################################################
if __name__ == '__main__':
    fire.Fire()
