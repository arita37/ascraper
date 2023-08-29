"""
pip install utilmy fire


"""
import os, csv, yaml, fire
from typing import List
from pydantic import BaseModel, Field

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.output_parsers import PydanticOutputParser


from utilmy import ( config_load, log, date_now, pd_read_file, pd_to_file

)


##############################################################################################
def csv_write(relations, output_file):
    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(relations)


class ListOfRelations(BaseModel):
    list_of_relations: List[List[str]] = Field("A list of [ENTITY1, ENTITY2, RELATION] lists.")



###########################################################################################################
def generate_kgraph(prompt=None, output_file=None, input_file=None, cfg='config.yml'):
    """ Extrapolates the relationships from the given prompt. 
    
    
    """

    config = config_load(cfg)
    
    if instance(input_file, str):
        with open(input_file, 'r') as f:
            prompt = f.read().strip()

    output_file = config['default_output'] if output_file is None else output_file 

    
    os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']
    chat   = ChatOpenAI(**config['model_params'])
    parser = PydanticOutputParser(pydantic_object=ListOfRelations)
    
    system_prompt_template = SystemMessagePromptTemplate.from_template(config['system_prompt_template'])
    human_prompt_template  = HumanMessagePromptTemplate.from_template("{prompt}")
    chat_prompt_template   = ChatPromptTemplate.from_messages([system_prompt_template, human_prompt_template])
    
    response = chat(chat_prompt_template.format_prompt(
        format_instructions=parser.get_format_instructions(),
        prompt=prompt
    ).to_messages()).content
    
    output = parser.parse(response).list_of_relations
    csv_write(output, output_file)



################################################################################################################
if __name__ == '__main__':
    init()
    fire.Fire()


