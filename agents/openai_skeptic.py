import openai, os
from dotenv import load_dotenv
load_dotenv()

def skeptic_response(claim):
    prompt = open("prompts/skeptic.txt").read().replace("{{CLAIM}}", claim)
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        api_key=os.getenv("OPENAI_API_KEY")
    )
    return response['choices'][0]['message']['content'].strip()
