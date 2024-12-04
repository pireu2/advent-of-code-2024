

INPUT_FILE = "input.in"


def is_safe(report):
    sig = -1 if report[0] > report[1] else 1
    for i in range(len(report) - 1):
        new_sig = -1 if report[i] > report[i+1] else 1
        difference = abs(report[i] - report[i+1])
        if difference < 1 or difference > 3 or sig != new_sig:
            return False

    return True

def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

def main():
    total = 0
    with open(INPUT_FILE, "r") as file:
        for line in file:
            report = [int(x) for x in line.split(" ")]
            if is_safe_with_dampener(report):
                total += 1

    print(total)


if __name__ == "__main__":
    main()