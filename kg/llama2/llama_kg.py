"""
Relations extractor powered by LLaMA-2-7B-chat model

# CPU llama-cpp-python
    pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir --verbose
# Dependencies:
    pip install utilmy fire langchain

#### Test Run
cd kg
python llama_kg.py generate_kgraph --prompt_name prompt1 -dirout llama_out.csv

Works with GGUF models (GGML models are deprecated)

"""

import ast, csv, fire
from utilmy import config_load, log

from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.chains import LLMChain


################################################################################
def hf_download(local_dir=None, repo_id=None, filename=None,
                cfg='llama_config.yml',  mode='mode1'):
    """
    Downloads specified model from hugging_face repo.

    python llama_kg.py  hf_donwload  --repo_id 'TheBloke/Llama-2-7B-GGUF'   --filename 'llama-2-7b.Q4_K_M.gguf'  --local_dir './models'

    local_dir: model save directory
    repo_id: id of the huggingface repo
    filename: name of the model file
    cfg: yaml cfg file
    mode: cfg file mode
    """
    if (repo_id and not filename) or (filename and not repo_id):
        raise ValueError("No full repo_path specified.")

    from huggingface_hub import hf_hub_download

    cfg  = config_load(cfg)
    cfg1 = cfg[mode]
    cfg2 = cfg1['model_source']

    repo_id   = repo_id   if repo_id   else cfg2.get('repo_id', 'TheBloke/Llama-2-7B-GGUF')
    filename  = filename  if filename  else cfg2.get('filename', 'llama-2-7b.Q4_K_M.gguf')
    local_dir = local_dir if local_dir else cfg2.get('local_dir', './models')

    model_path = hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        local_dir=local_dir,
    )
    log("Model's cache saved to ~/.cache")
    log(f"Path to the model: {model_path}")



def generate_kgraph(prompt=None, prompt_name='prompt1', model_path=None,
                    dirout="kg_out.csv", cfg='llama_config.yml', mode='mode1'):
    """
      Extrapolates the relationships from the given prompt.
      LLama-2-chat model support.
      Uses a fewshot prompt template, specified in the config file.

      prompt: prompt to extrapolate relations from
      prompt_name: name of the named prompt present in cfg file
      model_path: path to the llama-2-chat model
      dirout: output file path
      cfg: yaml cfg file
      mode: cfg file mode
    """
    cfg0 = config_load(cfg)
    cfg  = cfg0[mode]

    prompt1 = prompt if isinstance(prompt, str) else cfg[prompt_name]
    model_path = model_path if model_path else cfg.get('model_path')

    #### Load specific config ##################################################

    mkwargs = cfg.get('model_kwargs')
    prompt_template_params = cfg.get('prompt_template')
    example_template_params = cfg.get('prompt_template_example')

    #### Example and Main templates ############################################
    example_prompt = PromptTemplate(**example_template_params)
    prompt_template = FewShotPromptTemplate(
        **prompt_template_params,
        example_prompt=example_prompt
    )

    #### Model init and run ####################################################
    log(f"### Initializing model...")
    try:
        llm = LlamaCpp(
            model_path=model_path,
            **mkwargs
        )
        log(f'### Model successfully initialized')
    except Exception as e:
        log(f'### Error while initializing model: {e}')
        return

    log(f"### Running the model...")
    llm_chain = LLMChain(prompt=prompt_template, llm=llm)
    response = llm_chain.run(input=prompt1)

    #### Parsing the response ##################################################
    log("### Parsing response")
    try:
        output = parse_response(response)
        csv_write(output, dirout)
        log(f"Output written to {dirout}")
    except Exception as e:
        log(f"Error parsing the response: {e}")


################################################################################

##### utils ####################################################################
def csv_write(relations, dirout):
    with open(dirout, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['a', 'b', 'relation'])
        writer.writerows(relations)


def parse_response(response):
    start = response.index('[')
    relations_str = response[start:]
    relations = ast.literal_eval(relations_str)

    return relations


################################################################################
if __name__ == '__main__':
    commands = {
        'hf_download':  hf_download,
        "generate_kgraph": generate_kgraph
    }
    fire.Fire(commands)