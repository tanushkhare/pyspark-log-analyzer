from fastapi import APIRouter
from app.schemas.logs import LogAnalysisResponse
from app.services.spark_service import analyze_server_logs

router = APIRouter(prefix="/api", tags=["PySpark Log Analyzer"])

@router.get("/analyze", response_model=LogAnalysisResponse)
def get_log_analytics():
    return analyze_server_logs()