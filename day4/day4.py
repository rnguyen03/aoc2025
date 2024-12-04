# Define the X-MAS pattern
pattern = [
    (0, -1, 'M'),  # Top-left M
    (1, 0, 'A'),   # Middle A
    (2, -1, 'M'),  # Bottom-left M
    (0, 1, 'S'),   # Top-right S
    (2, 1, 'S')    # Bottom-right S
]

# Function to count X-MAS patterns
def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for x in range(rows - 2):  # At least 3 rows needed for the X
        for y in range(1, cols - 1):  # At least 2 columns on each side for the X
            # Check all conditions of the X-MAS pattern
            if all(
                0 <= x + dx < rows and 0 <= y + dy < cols and grid[x + dx][y + dy] == char
                for dx, dy, char in pattern
            ):
                count += 1
    return count


def count_xmas_patterns_2(grid):
    rows = len(grid)
    cols = len(grid[0])
    xmas_count = 0  # Counter for valid X-MAS patterns

    for x in range(1, rows - 1):  # Center "A" can't be on the first or last row
        for y in range(1, cols - 1):  # Center "A" can't be on the first or last column
            if grid[x][y] == "A":
                # Check if both diagonals are valid
                diagonal1 = {grid[x - 1][y - 1], grid[x + 1][y + 1]}
                diagonal2 = {grid[x - 1][y + 1], grid[x + 1][y - 1]}
                
                if diagonal1 == {"M", "S"} and diagonal2 == {"M", "S"}:
                    xmas_count += 1

    return xmas_count


# Main execution
file_path = "./file.txt"
with open(file_path, "r") as file:
    grid = [line.strip() for line in file.readlines()]

xmas_count = count_xmas_patterns(grid)
print("Part 1:")
print(f"Total X-MAS patterns found: {xmas_count}")

print()

xmas_count2 = count_xmas_patterns_2(grid)
print("Part 2:")
print(f"Total X-MAS patterns found: {xmas_count2}")
