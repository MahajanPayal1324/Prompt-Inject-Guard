
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
