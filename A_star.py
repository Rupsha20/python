import heapq

def a_star(graph, start, goal, h):
    open_list = []
    heapq.heappush(open_list, (0 + h(start), start))
    came_from = {start: None}
    g_score = {start: 0}
    f_score = {start: h(start)}
    
    while open_list:
        current = heapq.heappop(open_list)[1]
        
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor, weight in graph[current]:
            tentative_g_score = g_score[current] + weight
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None  # No path found

# Example graph: adjacency list with weights
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic function (example: straight-line distance)
h = lambda n: {'A': 7, 'B': 6, 'C': 2, 'D': 4, 'E': 3, 'F': 1, 'G': 0}[n]

# Run A* algorithm
start = 'A'
goal = 'G'
path = a_star(graph, start, goal, h)
print(f"Path found: {path}")
