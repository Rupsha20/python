import random
import math

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None, None

def get_moves(x, y):
    moves = []
    if x > 0: moves.append('up')
    if x < 2: moves.append('down')
    if y > 0: moves.append('left')
    if y < 2: moves.append('right')
    return moves

def move_tile(state, x, y, move):
    new_state = [row[:] for row in state]
    if move == 'up':
        new_state[x][y], new_state[x-1][y] = new_state[x-1][y], new_state[x][y]
    elif move == 'down':
        new_state[x][y], new_state[x+1][y] = new_state[x+1][y], new_state[x][y]
    elif move == 'left':
        new_state[x][y], new_state[x][y-1] = new_state[x][y-1], new_state[x][y]
    elif move == 'right':
        new_state[x][y], new_state[x][y+1] = new_state[x][y+1], new_state[x][y]
    return new_state

def h1(state, goal):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                misplaced += 1
    return misplaced

def h2(state, goal):
    distance = 0
    for i in range(1, 9):
        x1, y1 = find_position(state, i)
        x2, y2 = find_position(goal, i)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def find_position(state, value):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j
    return None, None

def simulated_annealing(initial, goal, heuristic, max_iterations=100000, initial_temp=1000, cooling_rate=0.999):
    current_state = initial
    current_cost = heuristic(current_state, goal)
    temperature = initial_temp

    for i in range(max_iterations):
        if current_state == goal:
            return current_state, i

        x, y = find_blank(current_state)
        move = random.choice(get_moves(x, y))
        new_state = move_tile(current_state, x, y, move)
        new_cost = heuristic(new_state, goal)

        delta_cost = new_cost - current_cost

        if delta_cost < 0 or random.uniform(0, 1) < math.exp(-delta_cost / temperature):
            current_state = new_state
            current_cost = new_cost

        temperature *= cooling_rate

        if temperature < 1e-10:
            break

    return None, max_iterations

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]

heuristic_choice = 'h2'
heuristic_func = h1 if heuristic_choice == 'h1' else h2

solution_state, iterations = simulated_annealing(initial_state, goal_state, heuristic_func)

print("Initial State:")
for row in initial_state:
    print(row)

if solution_state is not None:
    print("\nSolution found:")
    for row in solution_state:
        print(row)
    print(f"Number of iterations: {iterations}")
else:
    print("\nNo solution found. Try increasing iterations or changing the cooling rate.")
