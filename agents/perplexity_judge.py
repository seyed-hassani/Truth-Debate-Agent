import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("PERPLEXITY_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

def judge_response(claim, skeptic, supporter):
    prompt = open("prompts/judge.txt").read()
    prompt = prompt.replace("{{CLAIM}}", claim).replace("{{SKEPTIC}}", skeptic).replace("{{SUPPORTER}}", supporter)

    response = openai.ChatCompletion.create(
        model="perplexity/pplx-7b-chat",  # or use pplx-70b-chat if needed
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response['choices'][0]['message']['content'].strip()
