"""

pip install utilmy fire openai langchain

set OPENAI_API_KEY env variable

[test] python <__name__> generate_kgraph --prompt_name="prompt1" -o result.csv

"""
import ast, csv, fire
from utilmy import config_load, log

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate, FewShotPromptTemplate


##############################################################################################
def csv_write(relations, output_file):
    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Entity1', 'Entity2', 'Relation'])
        writer.writerows(relations)


###########################################################################################################
def generate_kgraph(prompt=None, prompt_name='prompt1', output_file=None, cfg='config.yml'):
    """ Extrapolates the relationships from the given prompt. 
        Uses a fewshot prompt template, specified in the config file.
    """

    config = config_load(cfg)

    if isinstance(prompt, str):
        prompt1 = prompt
    else:
        prompt1 = config[prompt_name]

    mpars = config['model_params']
    prompt_template_params = config['prompt_template']
    example_template_params = config['example_prompt_template']
    output_file = config['output'] if output_file is None else output_file

    #############################################################################
    log(f"Initializing model {mpars['model_name']}")
    model = OpenAI(**mpars)

    #### Context + template prompt ############################
    example_prompt = PromptTemplate(**example_template_params)
    prompt_template = FewShotPromptTemplate(
        **prompt_template_params,
        example_prompt=example_prompt,
    )
    log(f"Running the model")
    _input = prompt_template.format(input=prompt1)
    response = model(_input)
    log("Parsing the response")
    try:
        output = ast.literal_eval(response)
        csv_write(output, output_file)
        log(f"Output written to {output_file}")
    except Exception as e:
        log(f"Error editing the output: {e}")


################################################################################################################
if __name__ == '__main__':
    fire.Fire()
