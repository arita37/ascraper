"""



pip install utilmy fire

set OPENAI_API_KEY env variable

"""
import csv
import ast
import fire
from langchain import PromptTemplate
from utilmy import config_load
from typing import List

from langchain.llms import OpenAI
from langchain.prompts import FewShotPromptTemplate

from pydantic import BaseModel, Field


##############################################################################################
def csv_write(relations, output_file):
    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(relations)


###########################################################################################################
def generate_kgraph(prompt=None, prompt_name='prompt1', output_file=None, cfg='config.yml'):
    """ Extrapolates the relationships from the given prompt. """

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
    model = OpenAI(**mpars)

    #### Context + template prompt ############################
    example_prompt  = PromptTemplate(**example_template_params)
    prompt_template = FewShotPromptTemplate(
        **prompt_template_params,
        example_prompt=example_prompt,
    )


    _input   = prompt_template.format(input=prompt1)
    response = model(_input)
    output   = ast.literal_eval(response)
    csv_write(output, output_file)



################################################################################################################
if __name__ == '__main__':
    fire.Fire()
