import google.generativeai as genai, os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def supporter_response(claim):
    prompt = open("prompts/supporter.txt").read().replace("{{CLAIM}}", claim)
    response = model.generate_content(prompt)
    return response.text.strip()
