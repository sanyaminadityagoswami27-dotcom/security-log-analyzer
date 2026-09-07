from fastapi import FastAPI

from src.parser import parse_log_file
from src.detector import detect_brute_force
from src.ip_detector import detect_suspicious_ips
from src.risk_engine import calculate_risk


app = FastAPI(
    title="Security Log Analyzer API",
    description="API for the Security Log Analyzer and Threat Detection System",
    version="1.0.0"
)


LOG_FILE = "data/sample_logs.txt"


def get_alerts():
    logs = parse_log_file(LOG_FILE)

    alerts = detect_brute_force(logs)

    suspicious_ips = ["192.168.1.50"]

    ip_alerts = detect_suspicious_ips(
        logs,
        suspicious_ips
    )

    alerts.extend(ip_alerts)

    # Add risk information to every alert
    for alert in alerts:
        risk = calculate_risk(alert)

        alert["risk_score"] = risk["risk_score"]
        alert["risk_level"] = risk["risk_level"]

    return alerts


@app.get("/")
def root():
    return {
        "message": "Security Log Analyzer API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/alerts")
def get_security_alerts():
    alerts = get_alerts()

    return {
        "total_alerts": len(alerts),
        "alerts": alerts
    }