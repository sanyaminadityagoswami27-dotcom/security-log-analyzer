from datetime import datetime, timedelta
def detect_brute_force(logs, threshold=3, window_seconds=60):
    failed_attempts = {}
    alerts = []

    for log in logs:
        if log["event"] != "LOGIN_FAILED":
            continue

        ip = log["ip"]
        timestamp = datetime.strptime(
            log["timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )

        if ip not in failed_attempts:
            failed_attempts[ip] = []

        failed_attempts[ip].append(timestamp)

        cutoff_time = timestamp - timedelta(seconds=window_seconds)

        failed_attempts[ip] = [
            time for time in failed_attempts[ip]
            if time >= cutoff_time
        ]

        if len(failed_attempts[ip]) == threshold:
            alerts.append({
                "type": "BRUTE_FORCE",
                "ip": ip,
                "failed_attempts": threshold,
                "severity": "HIGH",
                "window_seconds": window_seconds
            })

    return alerts