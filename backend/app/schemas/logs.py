from pydantic import BaseModel

class LogAnalysisResponse(BaseModel):
    total_logs_processed: int
    error_count: int
    warning_count: int
    status: str
    top_ip_addresses: list