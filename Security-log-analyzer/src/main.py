from parser import parse_log_file
from detector import detect_brute_force
from risk_engine import calculate_risk
from ip_detector import detect_suspicious_ips
from report_generator import generate_report
LOG_FILE = "data/sample_logs.txt"


def main():
    logs = parse_log_file(LOG_FILE)

    print(f"Analyzed {len(logs)} log entries.")
    print()

    alerts = detect_brute_force(logs)
    suspicious_ips = ["192.168.1.50"]

    ip_alerts = detect_suspicious_ips(logs, suspicious_ips)

    alerts.extend(ip_alerts)
    report_file = "reports/security_report.txt"

    generate_report(alerts, report_file)

    print(f"Security report generated: {report_file}")
    if alerts:
        print("SECURITY ALERTS")
        print("-" * 40)

        for alert in alerts:
            print(f"Type: {alert['type']}")
            print(f"IP: {alert['ip']}")
            if "failed_attempts" in alert:
                print(f"Failed Attempts: {alert['failed_attempts']}")
            print(f"Severity: {alert['severity']}")
            
            risk = calculate_risk(alert)
            print(f"Risk Score: {risk['risk_score']}/100")
            print(f"Risk Level: {risk['risk_level']}")
            print()
    else:
        print("No suspicious activity detected.")
if __name__ == "__main__":
    main()