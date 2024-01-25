"""

LLM to generate a JSON
Fine some some small dataset

   Input:  3 lines of text
   Ouput:  JSON Text , json which can call some speficic API format (field: names)

   JSON format is fixed.
   Role of tuning is to increase the correctness of JSON ouput (with 99% correct)



###
  JsonFormer, ....



### Model:
    https://huggingface.co/Nexusflow/NexusRaven-13B

    https://huggingface.co/TheBloke/NexusRaven-13B-GGUF



#### fine tuning code
    https://colab.research.google.com/drive/1Enyy6dwOFC34PIiJ1zU6QBskHyrqkXUY

    https://brev.dev/blog/fine-tuning-mistral

    https://github.com/huggingface/peft


"""


##### 



def test1():
    # Please `pip install transformers accelerate`
    from transformers import pipeline

    pipeline = pipeline(
        "text-generation",
        model="Nexusflow/NexusRaven-13B",
        torch_dtype="auto",
        device_map="auto",
    )

    prompt_template = """
    <human>:
    OPTION:
    <func_start>def hello_world(n : int)<func_end>
    <docstring_start>
    \"\"\"
    Prints hello world to the user.

    Args:
    n (int) : Number of times to print hello world.
    \"\"\"
    <docstring_end>

    OPTION:
    <func_start>def hello_universe(n : int)<func_end>
    <docstring_start>
    \"\"\"
    Prints hello universe to the user.

    Args:
    n (int) : Number of times to print hello universe.
    \"\"\"
    <docstring_end>

    User Query: Question: {question}

    Please pick a function from the above options that best answers the user query and fill in the appropriate arguments.<human_end>
    """


    prompt = prompt_template.format(question="Please print hello world 10 times.")
    result = pipeline(prompt, max_new_tokens=100, return_full_text=False, 
                    do_sample=False)[0]["generated_text"]

    # Get the "Initial Call" only
    start_str = "Initial Answer: "
    end_str.  = "\nReflection: "
    start_idx = result.find(start_str) + len(start_str)
    end_idx   = result.find(end_str)
    function_call = result[start_idx: end_idx]
    print (f"Generated Call: {function_call}")











