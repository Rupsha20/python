def ao_star(graph, start, h):
    open_list = {start}
    solved = {}
    path = {}

    while open_list:
        current = min(open_list, key=lambda n: h(n))
        open_list.remove(current)
        path[current] = []

        for child in graph[current]:
            if all(solved.get(c) for c in child):  # If all successors are solved
                solved[current] = True
                path[current].append(child)
            else:
                open_list.update(child)

    return path

# Example graph: AND-OR graph with heuristic values
graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E'], ['F']],
    'C': [['G']],
    'D': [['H', 'I']],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

# Heuristic function
h = lambda n: {'A': 3, 'B': 2, 'C': 2, 'D': 1, 'E': 1, 'F': 1, 'G': 0, 'H': 0, 'I': 0}[n]

# Run AO* algorithm
start = 'A'
path = ao_star(graph, start, h)
print(f"Path found: {path}")
