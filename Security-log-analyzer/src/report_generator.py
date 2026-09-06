def generate_report(alerts, output_file):
    with open(output_file, "w") as file:
        file.write("SECURITY LOG ANALYZER REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Total Alerts: {len(alerts)}\n\n")

        for alert in alerts:
            file.write(f"Alert Type: {alert['type']}\n")
            file.write(f"IP Address: {alert['ip']}\n")
            file.write(f"Severity: {alert['severity']}\n")

            if "failed_attempts" in alert:
                file.write(
                    f"Failed Attempts: {alert['failed_attempts']}\n"
                )

            # Calculate risk information
            if alert["type"] == "BRUTE_FORCE":
                risk_score = 90
                risk_level = "CRITICAL"
            elif alert["type"] == "SUSPICIOUS_IP":
                risk_score = 40
                risk_level = "MEDIUM"
            else:
                risk_score = 0
                risk_level = "LOW"

            file.write(f"Risk Score: {risk_score}/100\n")
            file.write(f"Risk Level: {risk_level}\n")
            file.write("\n")