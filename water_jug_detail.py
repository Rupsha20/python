from collections import deque

def water_jug_problem(capacity1, capacity2, target):
    # Initialize the queue with the starting point (0, 0) and an empty path
    queue = deque([((0, 0), [])])
    visited = set([(0, 0)])  # Use a set to track visited states

    while queue:
        (jug1, jug2), path = queue.popleft()  # Get the current state and path

        # If we reach the target amount in either jug, return the path and state
        if jug1 == target or jug2 == target:
            return path + [(jug1, jug2)]

        # Generate all possible states from the current state
        states = [
            (capacity1, jug2),  # Fill jug1
            (jug1, capacity2),  # Fill jug2
            (0, jug2),          # Empty jug1
            (jug1, 0),          # Empty jug2
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),  # Pour jug1 into jug2
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1))   # Pour jug2 into jug1
        ]

        # Add new states to the queue if not already visited
        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [(jug1, jug2)]))

    return None  # Return None if no solution is found

if __name__ == "__main__":
    capacity1 = 4  # Capacity of the first jug
    capacity2 = 3  # Capacity of the second jug
    target = 2     # Target amount to measure

    result = water_jug_problem(capacity1, capacity2, target)
    
    if result:
        print("Solution steps:")
        for step in result:
            print(f"Jug1: {step[0]} litres, Jug2: {step[1]} litres")
        print(f"Final State: Jug1 has {result[-1][0]} litres, Jug2 has {result[-1][1]} litres")
    else:
        print("No solution found")
