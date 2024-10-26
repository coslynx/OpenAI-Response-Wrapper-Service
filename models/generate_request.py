from pydantic import BaseModel, validator

class GenerateRequest(BaseModel):
    model: str
    prompt: str
    temperature: float = 0.7
    max_tokens: int = 100

    @validator("model")
    def model_validation(cls, value):
        allowed_models = ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]  # Update with allowed models
        if value not in allowed_models:
            raise ValueError(f"Invalid model name. Allowed models: {allowed_models}")
        return value

    @validator("prompt")
    def prompt_validation(cls, value):
        if not isinstance(value, str):
            raise TypeError("Prompt must be a string")
        if len(value) > 4000:  # Adjust based on model limits
            raise ValueError("Prompt cannot exceed 4000 characters")
        return value

    @validator("temperature")
    def temperature_validation(cls, value):
        if value < 0 or value > 1:
            raise ValueError("Temperature must be between 0 and 1")
        return value

    @validator("max_tokens")
    def max_tokens_validation(cls, value):
        if value <= 0 or value > 4000:  # Adjust based on model limits
            raise ValueError("Max tokens must be between 1 and 4000")
        return value