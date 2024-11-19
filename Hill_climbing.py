import random

# Define the goal state and blank tile
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 'B']]

# Function to check if current state is goal state
def is_goal(state):
    return state == GOAL_STATE

# Heuristic h1: Number of displaced tiles
def heuristic_displaced(state):
    displaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 'B' and state[i][j] != GOAL_STATE[i][j]:
                displaced += 1
    return displaced

# Heuristic h2: Total Manhattan distance
def heuristic_manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 'B':
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(i - x) + abs(j - y)
    return distance

# Function to get the position of the blank tile
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 'B':
                return i, j

# Generate possible moves (up, down, left, right)
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    for nx, ny in directions:
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Hill climbing algorithm
def hill_climbing(start_state, heuristic):
    current = start_state
    while True:
        current_cost = heuristic(current)
        if is_goal(current):
            return current

        neighbors = get_neighbors(current)
        next_state = None
        next_cost = float('inf')

        for neighbor in neighbors:
            cost = heuristic(neighbor)
            if cost < next_cost:
                next_state, next_cost = neighbor, cost

        if next_cost >= current_cost:
            return current

        current = next_state

# Function to print the puzzle state
def print_state(state):
    for row in state:
        print(' '.join(str(cell) for cell in row))
    print()

# Example usage
start_state = [[1, 2, 3], [4, 6, 5], [7, 'B', 8]]

print("Start State:")
print_state(start_state)
#print("Using Heuristic h1 (Number of Displaced Tiles):")
solution = hill_climbing(start_state, heuristic_displaced)
print("Solution State with h1 (Misplaced Tiles):")
print_state(solution)

#print("Using Heuristic h2 (Manhattan Distance):")
solution = hill_climbing(start_state, heuristic_manhattan)
print("Solution State with h2 (Manhattan Distance):")
print_state(solution)
