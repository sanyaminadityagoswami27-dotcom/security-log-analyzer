def detect_suspicious_ips(logs, suspicious_ips):
    alerts = []
    detected_ips = set()

    for log in logs:
        ip = log["ip"]

        if ip in suspicious_ips and ip not in detected_ips:
            alerts.append({
                "type": "SUSPICIOUS_IP",
                "ip": ip,
                "user": log["user"],
                "severity": "MEDIUM"
            })

            detected_ips.add(ip)

    return alerts