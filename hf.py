import config
from huggingface_hub import InferenceClient
MODELS=getattr(config,"HF_MODELS",["openai/gpt-oss-120b","deepseek-ai/DeepSeek-V3","MiniMaxAI/MiniMax-M1-80k","Qwen/Qwen2.5-7B-Instruct","meta-llama/Llama-3.1-8B"])
def generate_response(prompt:str,temperature:float=0.3,max_tokens:int=512)->str:
    key=getattr(config,"HF_API_KEY",None)
    if not key:
        return "Error HF_API_KEY missing in config.py"
    last_err=None
    for m in MODELS:
        try:
            c=InferenceClient(model=m,token=key)
            r=c.chat_completion(
                messages=[{"role":"user","content":prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return r.choices[0].message.content
        except Exception as e:
            last_err=e
    return(
        "Hugging face model failed\n"
        f"Tried models: {MODELS}\n"
        "FIX\n"
        "1)Switch to groq by importing groq.py in main.py\n"
        "2)Replace Hugging face model in hf.py\n"
        ) 
