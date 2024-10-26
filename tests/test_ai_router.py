from fastapi.testclient import TestClient
from api.main import app
from routers.ai_router import ai_router
from models.generate_request import GenerateRequest
from models.generate_response import GenerateResponse
import pytest

client = TestClient(app)

@pytest.fixture
def generate_request_data():
    return {
        "model": "text-davinci-003",
        "prompt": "Write a short story about a cat.",
        "temperature": 0.7,
        "max_tokens": 100
    }

def test_ai_router_generate_success(generate_request_data):
    response = client.post("/api/v1/ai/generate", json=generate_request_data)
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["result"] is not None
    assert isinstance(response.json()["result"], str)

def test_ai_router_generate_invalid_model(generate_request_data):
    generate_request_data["model"] = "invalid-model"
    response = client.post("/api/v1/ai/generate", json=generate_request_data)
    assert response.status_code == 422

def test_ai_router_generate_invalid_prompt(generate_request_data):
    generate_request_data["prompt"] = 123  # Invalid prompt type
    response = client.post("/api/v1/ai/generate", json=generate_request_data)
    assert response.status_code == 422

def test_ai_router_generate_invalid_temperature(generate_request_data):
    generate_request_data["temperature"] = 2  # Invalid temperature value
    response = client.post("/api/v1/ai/generate", json=generate_request_data)
    assert response.status_code == 422

def test_ai_router_generate_invalid_max_tokens(generate_request_data):
    generate_request_data["max_tokens"] = -100  # Invalid max_tokens value
    response = client.post("/api/v1/ai/generate", json=generate_request_data)
    assert response.status_code == 422

def test_ai_router_generate_openai_error(monkeypatch, generate_request_data):
    def mock_completions_create(*args, **kwargs):
        raise Exception("Mock OpenAI Error")
    monkeypatch.setattr(ai_router.openai.completions, "create", mock_completions_create)
    response = client.post("/api/v1/ai/generate", json=generate_request_data)
    assert response.status_code == 500