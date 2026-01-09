from pydantic import BaseModel

class QuizRequest(BaseModel):
    url: str
