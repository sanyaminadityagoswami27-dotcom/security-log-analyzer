from src.ip_detector import detect_suspicious_ips


def test_suspicious_ip_detection():
    logs = [
        {
            "timestamp": "2026-09-06 10:00:00",
            "event": "LOGIN_FAILED",
            "user": "admin",
            "ip": "192.168.1.50"
        },
        {
            "timestamp": "2026-09-06 10:01:00",
            "event": "LOGIN_SUCCESS",
            "user": "aditya",
            "ip": "192.168.1.20"
        }
    ]

    suspicious_ips = ["192.168.1.50"]

    alerts = detect_suspicious_ips(logs, suspicious_ips)

    assert len(alerts) == 1
    assert alerts[0]["type"] == "SUSPICIOUS_IP"
    assert alerts[0]["ip"] == "192.168.1.50"