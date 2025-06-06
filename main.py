from agents.openai_skeptic import skeptic_response
from agents.gemini_supporter import supporter_response
from agents.perplexity_judge import judge_response
import json

if __name__ == "__main__":
    claim = input("Enter a news claim: ").strip()

    print("\n🤔 Getting Skeptic Argument...")
    skeptic = skeptic_response(claim)

    print("\n🟢 Getting Supporter Argument...")
    supporter = supporter_response(claim)

    print("\n⚖️ Judging the Debate...")
    verdict = judge_response(claim, skeptic, supporter)

    result = {
        "claim": claim,
        "skeptic_argument": skeptic,
        "supporter_argument": supporter,
        "verdict": verdict
    }

    with open("output/results.json", "w") as f:
        json.dump(result, f, indent=2)

    print("\n✅ Debate Complete! Result saved to `output/results.json`.")
