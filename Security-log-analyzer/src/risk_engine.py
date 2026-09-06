def calculate_risk(alert):
    score = 0

    if alert["type"] == "BRUTE_FORCE":
        score += 70
    if alert["type"] == "SUSPICIOUS_IP":
        score += 40
    if alert["severity"] == "HIGH":
        score += 20

    if alert.get("failed_attempts", 0) >= 5:
        score += 10

    if score >= 80:
        risk_level = "CRITICAL"
    elif score >= 60:
        risk_level = "HIGH"
    elif score >= 30:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "risk_score": score,
        "risk_level": risk_level
    }