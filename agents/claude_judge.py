import anthropic, os
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def judge_response(claim, skeptic, supporter):
    prompt = open("prompts/judge.txt").read()
    prompt = prompt.replace("{{CLAIM}}", claim).replace("{{SKEPTIC}}", skeptic).replace("{{SUPPORTER}}", supporter)

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text.strip()
