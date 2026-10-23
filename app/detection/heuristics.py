
import re


RULES = {
    "instruction_override": [
        r"ignore\s+(all\s+)?previous\s+instructions",
        r"ignore\s+(all\s+)?prior\s+instructions",
        r"disregard\s+(all\s+)?previous\s+instructions",
    ],
    "system_prompt_extraction": [
        r"reveal\s+(your\s+)?system\s+prompt",
        r"show\s+(me\s+)?(your\s+)?system\s+prompt",
        r"print\s+(your\s+)?system\s+prompt",
    ],
    "role_manipulation": [
        r"you\s+are\s+now\s+an?\s+",
        r"pretend\s+you\s+are\s+",
    ],
}


def detect_suspicious_patterns(prompt: str) -> dict:
    matched_rules = []

    for category, patterns in RULES.items():
        for pattern in patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                matched_rules.append(category)
                break

    if matched_rules:
        verdict = "FLAG"
    else:
        verdict = "SAFE"

    return {
        "verdict": verdict,
        "matched_rules": matched_rules,
        "risk_score": min(len(matched_rules) / 3, 1.0),
    }
