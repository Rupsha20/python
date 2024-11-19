import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue to store the (cost, node, path)
    pq = [(0, start, [])]  # Initial cost is 0, start node, empty path
    visited = set()  # To keep track of visited nodes

    while pq:
        cost, node, path = heapq.heappop(pq)  # Get the node with lowest cost

        # Skip if node is already visited
        if node in visited:
            continue

        # Update path and mark node as visited
        path = path + [node]
        visited.add(node)

        # Goal check
        if node == goal:
            return cost, path  # Return the cost and path to goal

        # Explore neighbors
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))  # Push with updated cost

    return float("inf"), []  # If goal is not reachable

# Example graph as an adjacency list where each node has a list of (neighbor, weight)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Test the function
start = 'A'
goal = 'D'
cost, path = uniform_cost_search(graph, start, goal)
print(f"Cost: {cost}, Path: {' -> '.join(path)}")
