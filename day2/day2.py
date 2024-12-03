def is_safe(report):
    """
    Check if a report is safe based on the given criteria:
    - Levels must either be all increasing or all decreasing.
    - Any two adjacent levels differ by at least 1 and at most 3.
    """
    levels = list(map(int, report.split()))
    differences = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]
    if all(-3 <= diff <= -1 for diff in differences) or all(1 <= diff <= 3 for diff in differences):
        return True
    return False

def count_safe_reports(file_path):
    """
    Count the number of safe reports in the given file.
    """
    with open(file_path, 'r') as file:
        data = file.readlines()
    safe_count = sum(is_safe(report.strip()) for report in data if report.strip())
    return safe_count

def is_safe_with_dampener(report):
    """
    Check if a report is safe either directly or by removing one level.
    """
    levels = list(map(int, report.split()))

    # Function to check if a sequence is safe
    def is_sequence_safe(seq):
        differences = [seq[i+1] - seq[i] for i in range(len(seq) - 1)]
        return all(-3 <= diff <= -1 for diff in differences) or all(1 <= diff <= 3 for diff in differences)

    # Check if the sequence is safe as is
    if is_sequence_safe(levels):
        return True

    # Check if removing one level makes it safe
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_sequence_safe(modified_levels):
            return True

    return False

def count_safe_reports_with_dampener(file_path):
    """
    Count the number of safe reports in the given file, considering the Problem Dampener.
    """
    with open(file_path, 'r') as file:
        data = file.readlines()
    safe_count = sum(is_safe_with_dampener(report.strip()) for report in data if report.strip())
    return safe_count

if __name__ == "__main__":
    file_path = "file.txt"
    safe_count = count_safe_reports_with_dampener(file_path)
    print(f"Number of safe reports with Problem Dampener: {safe_count}")