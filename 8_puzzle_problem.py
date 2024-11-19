from heapq import heappop, heappush

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def find_blank(tile):
    for i, row in enumerate(tile):
        if 0 in row:
            return i, row.index(0)

def valid_moves(x, y):
    moves = []
    if x > 0:
        moves.append('up')
    if x < 2:
        moves.append('down')
    if y > 0:
        moves.append('left')
    if y < 2:
        moves.append('right')
    return moves

def apply_move(tile, x, y, move):
    new_tile = [row[:] for row in tile]
    if move == 'up':
        new_tile[x][y], new_tile[x-1][y] = new_tile[x-1][y], new_tile[x][y]
    elif move == 'down':
        new_tile[x][y], new_tile[x+1][y] = new_tile[x+1][y], new_tile[x][y]
    elif move == 'left':
        new_tile[x][y], new_tile[x][y-1] = new_tile[x][y-1], new_tile[x][y]
    elif move == 'right':
        new_tile[x][y], new_tile[x][y+1] = new_tile[x][y+1], new_tile[x][y]
    return new_tile

# Heuristic functions
def h1(state, goal_state):
    return 0

def h2(state, goal_state):
    displaced = sum(state[i][j] != goal_state[i][j] for i in range(3) for j in range(3))
    return displaced - 1

def h3(state, goal_state):
    distance = 0
    for i in range(1, 9):
        x1, y1 = find_tile(state, i)
        x2, y2 = find_tile(goal_state, i)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def find_tile(state, value):
    for i, row in enumerate(state):
        if value in row:
            return i, row.index(value)

def h4(state, goal_state):
    return h3(state, goal_state) + 1  # Example of overestimating the cost

heuristics = {'h1': h1, 'h2': h2, 'h3': h3, 'h4': h4}

def a_star_search(initial_state, goal_state, heuristic_name):
    heuristic_func = heuristics[heuristic_name]

    open_list = []
    heappush(open_list, PuzzleNode(initial_state, cost=0, heuristic=heuristic_func(initial_state, goal_state)))
    closed_list = set()

    while open_list:
        current_node = heappop(open_list)
        closed_list.add(tuple(tuple(row) for row in current_node.state))

        if current_node.state == goal_state:
            path = []
            while current_node.parent is not None:
                path.append(current_node.move)
                current_node = current_node.parent
            return path[::-1]

        x, y = find_blank(current_node.state)
        for move in valid_moves(x, y):
            new_state = apply_move(current_node.state, x, y, move)
            if tuple(tuple(row) for row in new_state) in closed_list:
                continue
            new_cost = current_node.cost + 1
            new_node = PuzzleNode(new_state, current_node, move, new_cost, heuristic_func(new_state, goal_state))
            heappush(open_list, new_node)

    return None

initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7,8, 0]]

print("Initial State:")
for row in initial_state:
    print(row)
print("\nGoal State:")
for row in goal_state:
    print(row)

solution_path = a_star_search(initial_state, goal_state, 'h3')

if solution_path:
    current_state = initial_state
    print("\nSteps to reach the goal state:")
    for row in current_state:
        print(row)
    for move in solution_path:
        x, y = find_blank(current_state)
        current_state = apply_move(current_state, x, y, move)
        print(f"\nMove {move}:")
        for row in current_state:
            print(row)
else:
    print("No solution found.")
