from src.detector import detect_brute_force


def test_brute_force_detection():
    logs = [
        {
            "timestamp": "2026-09-06 10:00:00",
            "event": "LOGIN_FAILED",
            "user": "admin",
            "ip": "192.168.1.50"
        },
        {
            "timestamp": "2026-09-06 10:00:10",
            "event": "LOGIN_FAILED",
            "user": "admin",
            "ip": "192.168.1.50"
        },
        {
            "timestamp": "2026-09-06 10:00:20",
            "event": "LOGIN_FAILED",
            "user": "admin",
            "ip": "192.168.1.50"
        }
    ]

    alerts = detect_brute_force(logs)

    assert len(alerts) == 1
    assert alerts[0]["type"] == "BRUTE_FORCE"
    assert alerts[0]["ip"] == "192.168.1.50"
    assert alerts[0]["failed_attempts"] == 3
def test_no_brute_force_for_normal_activity():
    logs = [
        {
            "timestamp": "2026-09-06 10:00:00",
            "event": "LOGIN_FAILED",
            "user": "aditya",
            "ip": "192.168.1.20"
        },
        {
            "timestamp": "2026-09-06 10:30:00",
            "event": "LOGIN_SUCCESS",
            "user": "aditya",
            "ip": "192.168.1.20"
        }
    ]

    alerts = detect_brute_force(logs)

    assert len(alerts) == 0