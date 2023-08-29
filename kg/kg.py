import os
import csv
import yaml
import fire

from typing import List
from pydantic import BaseModel, Field

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.output_parsers import PydanticOutputParser


def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def csv_write(relations, output_file):
    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(relations)


class ListOfRelations(BaseModel):
    list_of_relations: List[List[str]] = Field("A list of [ENTITY1, ENTITY2, RELATION] lists.")


config = load_config('config.yml')

os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']
chat = ChatOpenAI(**config['model_params'])
parser = PydanticOutputParser(pydantic_object=ListOfRelations)
system_prompt_template = SystemMessagePromptTemplate.from_template(config['system_prompt_template'])
human_prompt_template = HumanMessagePromptTemplate.from_template("{prompt}")
chat_prompt_template = ChatPromptTemplate.from_messages([system_prompt_template, human_prompt_template])


def extrapolate(prompt, output_file=config['default_output']):
    """ Extrapolates the relationships from the given prompt. """

    response = chat(chat_prompt_template.format_prompt(
        format_instructions=parser.get_format_instructions(),
        prompt=prompt
    ).to_messages()).content
    output = parser.parse(response).list_of_relations
    csv_write(output, output_file)


def extrapolate_from_file(input_file, output_file=config['default_output']):
    """ Takes the input prompt from file. """

    try:
        with open(input_file, 'r') as f:
            prompt = f.read().strip()
    except OSError as e:
        print(f"Error reading the file: {e}")
    extrapolate(prompt, output_file)


if __name__ == '__main__':
    fire.Fire({
        'extrapolate': extrapolate,
        'extrapolate_file': extrapolate_from_file,
    })
