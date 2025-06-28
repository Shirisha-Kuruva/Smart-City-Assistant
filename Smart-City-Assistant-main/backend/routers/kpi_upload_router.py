from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/")
def upload_kpi_file(file: UploadFile = File(...)):
    return {"filename": file.filename, "status": "Received"}
