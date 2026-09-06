def parse_log_line(line):
    parts = line.strip().split()

    if len(parts) < 5:
        return None

    timestamp = parts[0] + " " + parts[1]
    event = parts[2]
    user = parts[3].split("=")[1]
    ip = parts[4].split("=")[1]

    return {
        "timestamp": timestamp,
        "event": event,
        "user": user,
        "ip": ip
    }


def parse_log_file(file_path):
    logs = []

    with open(file_path, "r") as file:
        for line in file:
            parsed_log = parse_log_line(line)

            if parsed_log:
                logs.append(parsed_log)

    return logs