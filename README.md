# ascraper
## LLaMA_KG

Relations extractor powered by LLaMA-2-7B-chat model 

## Installation

```sh
pip install utilmy fire langchain
pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir
```

## Test Run
```sh
cd kg
python llama_kg.py generate_kgraph --prompt_name prompt1 -dirout llama_out.csv
```