from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Feedback(BaseModel):
    username: str
    feedback: str

@router.post("/")
def receive_feedback(data: Feedback):
    return {"message": f"Thanks for your feedback, {data.username}!"}
