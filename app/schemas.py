from pydantic import BaseModel, Field

class GuardRequest(BaseModel):
    prompt: str = Field(
        min_length=1,
        max_length=5000,
        description="The prompt to check for prompt injection attacks.",
    )


class GuardResponse(BaseModel):
    request_id: str
    verdict: str
    message: str
