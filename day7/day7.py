import itertools

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = {}
    for line in lines:
        if ":" in line:
            target, numbers = line.split(":")
            target = int(target.strip())
            numbers = list(map(int, numbers.split()))
            data[target] = numbers
    return data

def evaluate_expression(numbers, operators):
    """
    Evaluate the expression left-to-right, including +, *, and || operators.
    """
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def can_satisfy(target, numbers, operators):
    """
    Determines if the target can be achieved by placing the specified operators
    between the numbers, evaluated left-to-right.
    """
    n = len(numbers) - 1
    for ops in itertools.product(operators, repeat=n):
        if evaluate_expression(numbers, ops) == target:
            return True
    return False

def calculate_calibration(file_path, operators):
    data = parse_input(file_path)
    total_calibration_result = 0
    for target, numbers in data.items():
        if can_satisfy(target, numbers, operators):
            total_calibration_result += target
    return total_calibration_result

if __name__ == "__main__":
    # Specify the input file path
    input_file = "file.txt"

    # Part 1: Only + and * operators
    part1_result = calculate_calibration(input_file, ['+', '*'])
    print(f"Part 1 Total Calibration Result: {part1_result}")

    # Part 2: +, *, and || operators
    part2_result = calculate_calibration(input_file, ['+', '*', '||'])
    print(f"Part 2 Total Calibration Result: {part2_result}")
