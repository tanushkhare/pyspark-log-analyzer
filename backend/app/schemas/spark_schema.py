from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class LogAnalysisRequest(BaseModel):
    batch_size: int = Field(default=5000, ge=100, le=100000, description="Log lines to process across Spark partitions")
    partition_count: int = Field(default=4, ge=1, le=32, description="Spark RDD/DataFrame partition count")
    log_format: Optional[str] = Field(default="combined", description="Log format: combined, json, or common")

class StatusCodeMetrics(BaseModel):
    status_200: int
    status_304: int
    status_404: int
    status_500: int

class LogAnalysisResponse(BaseModel):
    job_id: str
    records_processed: int
    partition_count: int
    throughput_eps: float
    status_codes: StatusCodeMetrics
    error_rate_pct: float
    error_spike_detected: bool
    top_flagged_endpoints: List[Dict[str, Any]]
    timestamp: str
