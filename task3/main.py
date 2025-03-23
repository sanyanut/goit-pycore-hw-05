import sys
from collections import Counter


def parse_log_line(line: str) -> dict:
    try:
        log_line = line.strip().split(" ", 3)
        message = log_line[3] if len(log_line) > 3 else None

        return {
            "date": log_line[0],
            "time": log_line[1],
            "level": log_line[2],
            "message": message,
        }

    except Exception as error:
        print(error)
        sys.exit()


def load_logs(file_path: str) -> list:
    try:
        logs_list = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line_dict = parse_log_line(line)
                logs_list.append(line_dict)
        return logs_list

    except Exception as error:
        print(error)
        sys.exit()
    except IndexError as error:
        print("Wrong file data format in log file!")
        sys.exit()


def filter_logs_by_level(logs: list, level: str) -> list:
    try:
        level = level.lower()
        log_list_by_level = list(
            filter(lambda log: log["level"].lower() == level, logs)
        )
        return log_list_by_level
    except Exception as error:
        print(error)
        sys.exit()


def count_logs_by_level(logs: list) -> dict:
    try:
        if not len(logs):
            print("Log file is empty")
            sys.exit()
        counts = Counter([log["level"] for log in logs])
        return dict(counts)
    except Exception as error:
        print(error)
        sys.exit()


def display_log_counts(counts: dict):
    try:
        col_1 = "Рівень логування"
        col_2 = "Кількість"
        col_divider = "|"
        col_1_len = len(col_1) + 1
        col_2_len = len(col_2) + 1
        print(f"{col_1 + " " + col_divider + " " + col_2}")
        print(f"{col_1_len * '-'}{col_divider}{col_2_len * '-'}")
        for log in counts:
            val = counts[log]
            log_len_space = col_1_len - len(log)
            print(f"{log + log_len_space * " " + col_divider + " "}{val}")
    except Exception as error:
        print(error)
        sys.exit()


if __name__ == "__main__":
    try:
        path = sys.argv[1]
        all_logs = load_logs(path)
        logs_by_level = count_logs_by_level(all_logs)
        if len(sys.argv) == 3 and sys.argv[2].upper() in logs_by_level:
            # check if 3 args are present and third arg fits the naming of the level
            display_log_counts(logs_by_level)
            filtered_logs = filter_logs_by_level(all_logs, sys.argv[2])
            print(f"Деталі логів для рівня '{sys.argv[2].upper()}':\n")
            for log in filtered_logs:
                print(f"{log["date"]} {log["time"]} - {log["message"]}")
        elif len(sys.argv) == 2:
            # check if there are two args
            display_log_counts(logs_by_level)
        else:
            print("Log analyzis requres Path and log Level as arguments")
    except Exception as error:
        print(error)
        sys.exit()
