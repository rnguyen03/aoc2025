# Read the map input from a file
file_path = "file.txt"

# Load the map from the file
with open(file_path, "r") as file:
    lab_map = [list(line.strip()) for line in file.readlines()]

# Determine the map dimensions
rows, cols = len(lab_map), len(lab_map[0])

# Define movement directions: up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (dy, dx)
direction_symbols = ["^", ">", "v", "<"]

# Find the starting position and initial direction
start_pos = None
current_direction = 0  # Default: facing up (^)
for r in range(rows):
    for c in range(cols):
        if lab_map[r][c] in direction_symbols:
            start_pos = (r, c)
            current_direction = direction_symbols.index(lab_map[r][c])
            break
    if start_pos:
        break

# Function for part 1: count distinct visited positions
def run(board, start_pos, direction):
    visited_positions = set()
    current_pos = start_pos
    visited_positions.add(current_pos)

    while True:
        dy, dx = directions[direction]
        next_pos = (current_pos[0] + dy, current_pos[1] + dx)

        # Check bounds
        if next_pos[0] < 0 or next_pos[0] >= rows or next_pos[1] < 0 or next_pos[1] >= cols:
            break  # Exits the map
        if board[next_pos[0]][next_pos[1]] == "#":
            direction = (direction + 1) % 4  # Turn right
        else:
            current_pos = next_pos
            visited_positions.add(current_pos)
    
    return len(visited_positions)

# Function for part 2: simulate loop detection
def run2(board, start_pos, direction):
    seen_states = set()
    current_pos = start_pos

    while True:
        state = (current_pos[0], current_pos[1], direction)
        if state in seen_states:
            return True  # Loop detected
        seen_states.add(state)

        dy, dx = directions[direction]
        next_pos = (current_pos[0] + dy, current_pos[1] + dx)

        if next_pos[0] < 0 or next_pos[0] >= rows or next_pos[1] < 0 or next_pos[1] >= cols:
            break  # Exits the map
        if board[next_pos[0]][next_pos[1]] == "#":
            direction = (direction + 1) % 4  # Turn right
        else:
            current_pos = next_pos

    return False

# Main execution
def main(board, part2=False):
    global start_pos, current_direction
    if not part2:
        return run(board, start_pos, current_direction)
    else:
        ret = 0
        for y in range(rows):
            for x in range(cols):
                if board[y][x] == ".":
                    board[y][x] = "#"  # Temporarily block
                    if run2(board, start_pos, current_direction):
                        ret += 1
                    board[y][x] = "."  # Restore
        return ret

# Solve for both parts
result_part1 = main(lab_map)
print("Part 1:", result_part1)

result_part2 = main(lab_map, part2=True)
print("Part 2:", result_part2)
