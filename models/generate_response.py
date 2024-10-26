from pydantic import BaseModel, Field

class GenerateResponse(BaseModel):
    """
    Defines the structure and validation rules for the API response when generating text using the OpenAI API.

    Attributes:
        success (bool): Indicates whether the text generation was successful.
        message (str, optional):  An error message if `success` is `False`, explaining the reason for failure.
        result (str): The generated text, returned as a string if `success` is `True`.

    Example:
        ```json
        {
            "success": true,
            "result": "This is the generated text."
        }
        ```
    """
    success: bool = Field(..., description="Indicates whether the text generation was successful.")
    message: str = Field(None, description="An error message if `success` is `False`")
    result: str = Field(..., description="The generated text, returned as a string if `success` is `True`")