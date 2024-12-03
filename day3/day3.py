def calculate_sum_with_conditions(memory_string):
    results = []
    mul_enabled = True  # Initially, mul instructions are enabled
    i = 0
    n = len(memory_string)
    
    while i < n:
        # Check for `do()` or `don't()`
        if memory_string[i:i+4] == "do()":
            mul_enabled = True
            i += 4  # Skip over "do()"
            continue
        elif memory_string[i:i+7] == "don't()":
            mul_enabled = False
            i += 7  # Skip over "don't()"
            continue
        
        # Look for 'mul('
        if memory_string[i:i+4] == 'mul(':
            start = i + 4  # Start after 'mul('
            end = start
            while end < n and memory_string[end] != ')':  # Find closing parenthesis
                end += 1
            
            if end < n:  # Ensure ')' was found
                # Extract the potential arguments
                content = memory_string[start:end]
                if ',' in content:
                    parts = content.split(',')
                    if len(parts) == 2:
                        x, y = parts[0].strip(), parts[1].strip()
                        # Validate both parts as integers with 1-3 digits
                        if x.isdigit() and y.isdigit() and 1 <= len(x) <= 3 and 1 <= len(y) <= 3:
                            if mul_enabled:  # Only add if mul is enabled
                                results.append(int(x) * int(y))
        i += 1  # Move to the next character

    return sum(results)

# Example usage
# Read the corrupted memory string from file
file_path = "./file.txt"
with open(file_path, "r") as file:
    corrupted_memory = file.read()

# Calculate the sum of valid enabled multiplications
result = calculate_sum_with_conditions(corrupted_memory)
print("The sum of all enabled mul operations is:", result)


# Part 1
# def parse_valid_muls_no_regex(memory_string):
#     results = []
#     i = 0
#     n = len(memory_string)
    
#     while i < n:
#         # Look for 'mul('
#         if memory_string[i:i+4] == 'mul(':
#             start = i + 4  # Start after 'mul('
#             end = start
#             while end < n and memory_string[end] != ')':  # Find closing parenthesis
#                 end += 1
            
#             if end < n:  # Ensure ')' was found
#                 # Extract the potential arguments
#                 content = memory_string[start:end]
#                 if ',' in content:
#                     parts = content.split(',')
#                     if len(parts) == 2:
#                         x, y = parts[0].strip(), parts[1].strip()
#                         # Validate both parts as integers with 1-3 digits
#                         if x.isdigit() and y.isdigit() and 1 <= len(x) <= 3 and 1 <= len(y) <= 3:
#                             results.append((int(x), int(y)))
#         i += 1  # Move to the next character

#     return results