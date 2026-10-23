import threading
import webbrowser

from app.schemas import GuardRequest, GuardResponse
from app.detection.heuristics import detect_suspicious_patterns
import uuid
from fastapi import FastAPI

app = FastAPI(
    title="PromptInjectGuard",
    description="A hybrid prompt injection detection and prevention system for local LLMs.",
    version="0.1.0",
)


@app.get("/")

def home():
    return {
        "message": "PromptInjectGuard API is running!",
        "status": "active",
    }


@app.get("/health")

def health_check():
    return {
        "status": "healthy",
    }


@app.post("/v1/guard", response_model=GuardResponse)
def guard_prompt(request: GuardRequest):
    result = detect_suspicious_patterns(request.prompt)

    return GuardResponse(
        request_id=str(uuid.uuid4()),
        verdict=result["verdict"],
        message=(
            f"Suspicious patterns detected: {', '.join(result['matched_rules'])}"
            if result["matched_rules"]
            else "No known suspicious patterns detected."
        ),
    )

if __name__ == "__main__":
    threading.Timer(
        2,
        lambda: webbrowser.open("http://127.0.0.1:8000/docs")
    ).start()

     