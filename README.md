# ascraper
## LLaMA_KG

Relations extractor powered by LLaMA-2-7B-chat model 


## Installation

### Model Download
```sh
pip install hugginggface_hub
```
```sh
from huggingface_hub import hf_hub_download
hf_hub_download(
    repo_id='TheBloke/Llama-2-7B-GGUF',
    filename='llama-2-7b.Q4_K_M.gguf',
    local_dir='./models'
)
```
Note: huggingface donwloads model cache to C://Users//<user>//.cache directory
	
### Dependencies
```sh
pip install utilmy fire langchain
pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir
```

## Test Run
```sh
cd kg
python llama_kg.py generate_kgraph --prompt_name prompt1 -dirout llama_out.csv
```