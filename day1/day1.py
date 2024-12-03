# Load the file and calculate the total distance based on the problem statement
from collections import Counter
# Define the function to calculate total distance
def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)

    # Calculate the total distance
    total_distance = sum(abs(left - right) for left, right in zip(left_list_sorted, right_list_sorted))
    return total_distance

# Load the file and parse the data
file_path = './file.txt'
left_list = []
right_list = []

with open(file_path, 'r') as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

# Calculate the total distance
total_distance = calculate_total_distance(left_list, right_list)
print(total_distance)

# Calculate the similarity score
def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_count = Counter(right_list)

    # Calculate the similarity score
    similarity_score = sum(num * right_count[num] for num in left_list)
    return similarity_score

# Calculate the similarity score for the provided lists
similarity_score = calculate_similarity_score(left_list, right_list)
print(similarity_score)
