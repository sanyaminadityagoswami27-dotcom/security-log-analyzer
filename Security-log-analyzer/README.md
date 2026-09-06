# Security Log Analyzer & Threat Detection System

A Python-based defensive cybersecurity tool that analyzes authentication logs, detects suspicious activity, calculates risk levels, and generates security reports.

## Features

- Authentication log parsing
- Time-window brute-force detection
- Suspicious IP detection
- Duplicate-alert prevention
- Risk scoring
- Risk-level classification
- Automated security report generation
- Automated unit testing

## Architecture

```text
Raw Authentication Logs
          |
          v
      Log Parser
          |
          v
   Detection Engine
      /        \
     v          v
Brute Force   Suspicious IP
     \          /
      v        v
       Alerts
          |
          v
     Risk Engine
          |
          v
   Security Report
## Project Structure

```text
security-log-analyzer/
|
├── data/
│   └── sample_logs.txt
|
├── reports/
│   └── security_report.txt
|
├── src/
│   ├── parser.py
│   ├── detector.py
│   ├── ip_detector.py
│   ├── risk_engine.py
│   ├── report_generator.py
│   ├── main.py
│   └── test_parser.py
|
├── tests/
│   ├── test_detector.py
│   └── test_ip_detector.py
|
└── README.md
## Technologies

Python
Git
GitHub
Pytest

## Detection Logic

Brute-Force Detection
The system tracks failed login attempts from each IP address.
A brute-force alert is generated when:
3 failed login attempts
within 60 seconds
from the same IP
Suspicious IP Detection
The system compares IP addresses found in authentication logs against a configured list of suspicious IP addresses.

## Risk Scoring

| Detection          | Score |
| ------------------ | ----: |
| Brute Force        |    70 |
| High Severity      |   +20 |
| 5+ Failed Attempts |   +10 |
| Suspicious IP      |    40 |

Risk levels:
80+  → CRITICAL
60+  → HIGH
30+  → MEDIUM
<30  → LOW

## Example Output

SECURITY ALERTS
----------------------------------------

Type: BRUTE_FORCE
IP: 192.168.1.50
Failed Attempts: 3
Severity: HIGH
Risk Score: 90/100
Risk Level: CRITICAL

Type: SUSPICIOUS_IP
IP: 192.168.1.50
Severity: MEDIUM
Risk Score: 40/100
Risk Level: MEDIUM

## Security Report
The application automatically generates:
reports/security_report.txt
The report contains detected alerts, IP addresses, severity levels, failed-attempt information, and risk scores.

## Testing
Run all automated tests:
python -m pytest tests/
Expected result:
3 passed

## How to Run
From the project root:
python src/main.py
The application will analyze the sample logs, detect suspicious activity, display security alerts, and generate a security report.

## Future Improvements
Real-time log monitoring
More authentication attack detection rules
Windows/Linux log support
JSON report generation
Web-based security dashboard
SIEM integration
IP reputation integration
Advanced anomaly detection

## Disclaimer
This project is designed for defensive cybersecurity learning and authorized security analysis only.

### Important ⚠️
Notice that the last line is:
```text

**You should NOT add another closing ``` after the entire README.**

The closing ``` immediately after the **Project Structure** section closes that particular code block. The other code blocks throughout the README open and close themselves.

