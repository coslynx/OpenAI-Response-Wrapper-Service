import pytest
from utils.generate_text import generate_text
from models.generate_request import GenerateRequest
from models.generate_response import GenerateResponse
from openai import OpenAI
from fastapi import HTTPException
from unittest.mock import MagicMock

# Define a sample GenerateRequest object for testing purposes.
@pytest.fixture
def generate_request_data():
    return GenerateRequest(
        model="text-davinci-003",
        prompt="Write a short story about a cat.",
        temperature=0.7,
        max_tokens=100
    )

# Test successful text generation using the generate_text function.
def test_generate_text_success(generate_request_data):
    # Create a mock OpenAI client.
    mock_openai = MagicMock(spec=OpenAI)
    mock_openai.completions.create.return_value = {
        "choices": [{"text": "This is a sample cat story."}]
    }

    # Replace the actual OpenAI client with the mock client.
    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr(generate_text, "openai", mock_openai)

    # Call the generate_text function and check the response.
    response = generate_text(generate_request_data)
    assert isinstance(response, GenerateResponse)
    assert response.success is True
    assert response.result == "This is a sample cat story."

# Test error handling in the generate_text function when the OpenAI API call fails.
def test_generate_text_openai_error(generate_request_data):
    # Create a mock OpenAI client that raises an exception.
    mock_openai = MagicMock(spec=OpenAI)
    mock_openai.completions.create.side_effect = Exception("Mock OpenAI Error")

    # Replace the actual OpenAI client with the mock client.
    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr(generate_text, "openai", mock_openai)

    # Call the generate_text function and verify that a HTTPException is raised.
    with pytest.raises(HTTPException) as excinfo:
        generate_text(generate_request_data)

    # Verify the status code and error message of the HTTPException.
    assert excinfo.value.status_code == 500
    assert "Error generating text: Mock OpenAI Error" in str(excinfo.value.detail)

# Test the validation logic for invalid models in the generate_text function.
def test_generate_text_invalid_model(generate_request_data):
    generate_request_data.model = "invalid-model"

    # Call the generate_text function and verify that a ValueError is raised.
    with pytest.raises(ValueError) as excinfo:
        generate_text(generate_request_data)

    # Verify the error message of the ValueError.
    assert "Invalid model name" in str(excinfo.value)

# Test the validation logic for invalid prompts in the generate_text function.
def test_generate_text_invalid_prompt(generate_request_data):
    generate_request_data.prompt = 123  # Invalid prompt type

    # Call the generate_text function and verify that a TypeError is raised.
    with pytest.raises(TypeError) as excinfo:
        generate_text(generate_request_data)

    # Verify the error message of the TypeError.
    assert "Prompt must be a string" in str(excinfo.value)

# Test the validation logic for invalid temperatures in the generate_text function.
def test_generate_text_invalid_temperature(generate_request_data):
    generate_request_data.temperature = 2  # Invalid temperature value

    # Call the generate_text function and verify that a ValueError is raised.
    with pytest.raises(ValueError) as excinfo:
        generate_text(generate_request_data)

    # Verify the error message of the ValueError.
    assert "Temperature must be between 0 and 1" in str(excinfo.value)

# Test the validation logic for invalid max_tokens in the generate_text function.
def test_generate_text_invalid_max_tokens(generate_request_data):
    generate_request_data.max_tokens = -100  # Invalid max_tokens value

    # Call the generate_text function and verify that a ValueError is raised.
    with pytest.raises(ValueError) as excinfo:
        generate_text(generate_request_data)

    # Verify the error message of the ValueError.
    assert "Max tokens must be between 1 and 4000" in str(excinfo.value)