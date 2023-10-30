


import os
import logging
from ludwig.api import LudwigModel
import yaml
import logging
from ludwig.api import LudwigModel
from ludwig.datasets import agnews
import ludwig.datasets
import pandas as pd

# Load the YAML configuration
with open('LLama_config.yaml', 'r') as file:
    model_config = yaml.safe_load(file)

os.environ["HUGGING_FACE_HUB_TOKEN"] = ""


model = LudwigModel(model_config, logging_level=logging.INFO)
results = model.train(dataset="./AG_NEWS_DATA.txt")
print(results)



