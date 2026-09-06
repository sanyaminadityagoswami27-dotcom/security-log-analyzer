from parser import parse_log_file


file_path = "data/sample_logs.txt"

logs = parse_log_file(file_path)

for log in logs:
    print(log)