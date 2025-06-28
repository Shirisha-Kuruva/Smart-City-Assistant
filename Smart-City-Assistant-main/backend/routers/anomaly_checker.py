from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AnomalyRequest(BaseModel):
    metric: str
    value: float

@router.post("/")
def check_anomaly(data: AnomalyRequest):
    if data.value > 100:
        return {"anomaly": True, "metric": data.metric}
    return {"anomaly": False, "metric": data.metric}
