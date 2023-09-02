"""

pip install utilmy fire openai langchain


export OPENAI_API_KEY=""    # env variable
cd kg
python kg.py generate_kgraph --prompt_name prompt1  -o result.csv



"""
import ast, csv, fire
from utilmy import config_load, log

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate, FewShotPromptTemplate


##############################################################################################
def csv_write(relations, output_file):
    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['a', 'b', 'relation'])
        writer.writerows(relations)


##############################################################################################
def generate_kgraph(prompt=None, prompt_name='prompt1', mode='mode1', output_file="kg_out.csv", cfg='config.yml'):
    """ Extrapolates the relationships from the given prompt. 
        Uses a fewshot prompt template, specified in the config file.
    """
    config = config_load(cfg)

    
    prompt1 = prompt if isinstance(prompt, str) else prompt1 = config[prompt_name]


    #### Load specific config #################################
    cfg   = config[mode]
    mpars = cfg['model_params']
    prompt_template_params  = cfg['prompt_template']
    example_template_params = cfg['prompt_template_example']


    #############################################################################
    #### Context + template prompt ##############################################
    example_prompt = PromptTemplate(**example_template_params)
    prompt_template = FewShotPromptTemplate(
        **prompt_template_params,
        example_prompt=example_prompt,
    )


    log(f"### Running the model  {mpars['model_name']} ")
    _input = prompt_template.format(input=prompt1)
    model  = OpenAI(**mpars)
    response = model(_input)
    
    
    log("### Parsing response")
    try:
        output = ast.literal_eval(response)
        csv_write(output, output_file)
        log(f"Output written to {output_file}")
    except Exception as e:
        log(f"Error editing the output: {e}")









################################################################################################################
if __name__ == '__main__':
    fire.Fire()
