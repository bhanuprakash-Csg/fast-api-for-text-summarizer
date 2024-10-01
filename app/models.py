from pydantic import BaseModel

# Model for text input
class TextRequest(BaseModel):
    text: str
    style: str
