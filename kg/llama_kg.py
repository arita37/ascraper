"""
Works with GGUF models (GGML models are deprecated)

# CPU llama-cpp-python
    pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir --verbose
# Dependencies:
    pip install utilmy fire langchain

python llama_kg.py generate_kgraph --prompt_name prompt1 -dirout llama_out.csv
"""

import ast, csv, fire
from utilmy import config_load, log

from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.chains import LLMChain


################################################################################

def generate_kgraph(prompt=None, prompt_name='prompt1', dirout="kg_out.csv", cfg='llama_config.yml'):
    """
      Extrapolates the relationships from the given prompt.
      Uses a fewshot prompt template, specified in the config file.
    """
    cfg = config_load(cfg)

    prompt1 = prompt if isinstance(prompt, str) else cfg[prompt_name]

    #### Load specific config ##################################################

    mpars = cfg['model_kwargs']
    prompt_template_params = cfg['prompt_template']
    example_template_params = cfg['prompt_template_example']

    #### Example and Main templates ############################################
    example_prompt = PromptTemplate(**example_template_params)
    prompt_template = FewShotPromptTemplate(
        **prompt_template_params,
        example_prompt=example_prompt
    )

    #### Model init and run ####################################################
    log(f"### Initializing model...")
    try:
        llm = LlamaCpp(**mpars)
        log(f'### Model successfuly initialized')
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
    fire.Fire()