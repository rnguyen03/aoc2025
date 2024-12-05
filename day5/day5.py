from collections import defaultdict, deque

def parse_rules(rules):
    graph = defaultdict(set)
    for rule in rules:
        X, Y = map(int, rule.split('|'))
        graph[X].add(Y)
    return graph

def is_valid_update(graph, update):
    # Extract a subset of the graph for the update pages
    subset_graph = defaultdict(set)
    indegree = defaultdict(int)
    
    for u in update:
        if u in graph:
            for v in graph[u]:
                if v in update:
                    subset_graph[u].add(v)
                    indegree[v] += 1
    
    # Topological sort to verify order
    queue = deque([u for u in update if indegree[u] == 0])
    sorted_order = []
    
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in subset_graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # If the sorted order matches the update, it's valid
    return sorted_order == update

def correct_update(graph, update):
    # Extract a subset of the graph for the update pages
    subset_graph = defaultdict(set)
    indegree = defaultdict(int)
    
    for u in update:
        if u in graph:
            for v in graph[u]:
                if v in update:
                    subset_graph[u].add(v)
                    indegree[v] += 1
    
    queue = deque([u for u in update if indegree[u] == 0])
    sorted_order = []
    
     # Topological sort to verify order
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in subset_graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # If the sorted order matches the update, it's valid
    return sorted_order

def find_middle_pages(updates):
    middle_sum = 0
    for update in updates:
        middle_index = len(update) // 2
        middle_sum += update[middle_index]
    return middle_sum

def solve_parts(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')
    
    # Separate rules and updates
    blank_line_index = lines.index('')
    rules = lines[:blank_line_index]
    updates = lines[blank_line_index + 1:]
    
    # Parse rules into a graph
    graph = parse_rules(rules)
    correct_updates = []
    incorrect_updates = []
    
    for update in updates:
        update_list = list(map(int, update.split(',')))
        if is_valid_update(graph, update_list):
            correct_updates.append(update_list)
        else:
            corrected_update = correct_update(graph, update_list)
            incorrect_updates.append(corrected_update)
    
    part1_result = find_middle_pages(correct_updates)
    
    part2_result = find_middle_pages(incorrect_updates)
    
    return part1_result, part2_result

filename = 'file.txt'
part1_result, part2_result = solve_parts(filename)
print("Part 1 - Sum of middle pages for correctly-ordered updates:", part1_result)
print("Part 2 - Sum of middle pages for corrected updates:", part2_result)
