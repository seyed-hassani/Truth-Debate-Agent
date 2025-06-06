# Truth Debate Agent
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-ff69b4?logo=openai)
![Gemini](https://img.shields.io/badge/Gemini-Pro-orange)
![Claude](https://img.shields.io/badge/Claude-3.5-yellowgreen?logo=Anthropic)

A multi-agent AI system that evaluates the truthfulness of news claims using:
- 🤖 OpenAI (Skeptic)
- 🤖 Gemini (Supporter)
- 🤖 Claude (Judge)

## How It Works
1. Input a news claim.
2. Skeptic (OpenAI) refutes the claim.
3. Supporter (Gemini) defends the claim.
4. Judge (Claude) evaluates both and gives:
   - Verdict: TRUE / FALSE / UNCERTAIN
   - Confidence score
   - Summary reasoning

## How to Run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Environment Variables
Store API keys in a `.env` file (do NOT upload it):
```
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
ANTHROPIC_API_KEY=your_claude_key
```
