from fastapi import FastAPI
from backend.routers.chat_router import router as chat_router
from backend.routers.feedback_router import router as feedback_router
from backend.routers.eco_tips_router import router as eco_tips_router
from backend.routers.kpi_upload_router import router as kpi_upload_router
from backend.routers.anomaly_checker import router as anomaly_checker
from backend.routers.vector_router import router as vector_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is working!"}

app.include_router(chat_router, prefix="/chat", tags=["Chat"])
app.include_router(feedback_router, prefix="/feedback", tags=["Feedback"])
app.include_router(eco_tips_router, prefix="/eco", tags=["Eco Tips"])
app.include_router(kpi_upload_router, prefix="/kpi", tags=["KPI Upload"])
app.include_router(anomaly_checker, prefix="/anomaly", tags=["Anomaly Checker"])
app.include_router(vector_router, prefix="/vector", tags=["Vector Search"])
