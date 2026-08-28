import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_spark_log_analysis_post():
    payload = {"batch_size": 10000, "partition_count": 8, "log_format": "combined"}
    res = client.post("/api/v1/logs/analyze", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "SPARK-" in data["job_id"]
    assert data["records_processed"] == 10000
    assert data["status_codes"]["status_200"] > 0
    assert len(data["top_flagged_endpoints"]) > 0

def test_spark_get_fallback():
    res = client.get("/api/v1/logs/analyze")
    assert res.status_code == 200
    data = res.json()
    assert data["throughput_eps"] > 0
