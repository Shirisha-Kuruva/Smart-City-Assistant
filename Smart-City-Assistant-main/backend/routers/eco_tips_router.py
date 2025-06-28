from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_eco_tips():
    return {"tips": ["Turn off lights when not in use", "Use public transport", "Reduce plastic usage"]}
