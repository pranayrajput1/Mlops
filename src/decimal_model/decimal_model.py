from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
import torch


def get_quantization_config(boolean_input: bool):
    if boolean_input:
        return dict(quantization_config=BitsAndBytesConfig(
            load_in_8bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16
        ))
    else:
        return dict(torch_dtype="auto")


def get_decimal_pipeline(model_name: str):
    print("Getting quantization configuration")
    dtype_kwargs = get_quantization_config(boolean_input=True)

    print(f"Loading Model: {model_name}")
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        trust_remote_code=True,
        **dtype_kwargs
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token

    print("Creating Pipeline")
    deci_generator = pipeline("text-generation",
                              model=model,
                              tokenizer=tokenizer,
                              temperature=0.1,
                              device_map="auto",
                              max_length=4096,
                              return_full_text=False)
    print("Returning decimal model pipeline adn tokenizer")
    return deci_generator, tokenizer


def get_decimal_response(deci_generator, tokenizer, system_prompt, user_prompt) -> str:
    prompt = tokenizer.apply_chat_template([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ], tokenize=False, add_generation_prompt=True)

    print("Getting response from model")
    response = deci_generator(prompt)[0]['generated_text']
    return str(response)
