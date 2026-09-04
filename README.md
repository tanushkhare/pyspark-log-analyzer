# ⚡ PySpark Distributed Log Analyzer

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://pyspark-log-analyzer-web.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://pyspark-log-analyzer-web.vercel.app](https://pyspark-log-analyzer-web.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Distributed batch processing engine computing RDD partition metrics, HTTP status code distributions, and anomaly patterns across large web server access logs.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** PySpark, Apache Spark, FastAPI, Python
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🛡️ Production Standards
* **HTTP Methods Aligned:** Fixed 404 mismatch by standardizing ingestion on POST endpoints.
* **SparkSession Ingestion:** Real partitioned RDD/DataFrame processing across 8 executor cores.
* **Error Distribution Breakdown:** Computes status distribution across HTTP 200, 404, and 500 status codes.

---

## 🚀 API Contracts
```http
POST /api/v1/logs/analyze
Request:
{
  "batch_size": 250000,
  "partition_count": 8
}

Response (200 OK):
{
  "status": "SUCCESS",
  "records_analyzed": 250000,
  "elapsed_ms": 184,
  "status_distribution": {
    "200": 232150,
    "404": 12400,
    "500": 5450
  }
}

GET /health
Response: {"status": "healthy"}

💻 Local Quickstart

Bash

pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v