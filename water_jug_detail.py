from collections import deque

def water_jug_problem(capacity1, capacity2, target):
    queue = deque([((0, 0), [])])
    visited = set([(0, 0)])  

    while queue:
        (jug1, jug2), path = queue.popleft() 

        if jug1 == target or jug2 == target:
            return path + [(jug1, jug2)]

        states = [
            (capacity1, jug2),  
            (jug1, capacity2),  
            (0, jug2),          
            (jug1, 0),         
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)), 
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1))   
        ]
        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [(jug1, jug2)]))

    return None 

if __name__ == "__main__":
    capacity1 = 4 
    capacity2 = 3
    target = 2     

    result = water_jug_problem(capacity1, capacity2, target)
    
    if result:
        print("Solution steps:")
        for step in result:
            print(f"Jug1: {step[0]} litres, Jug2: {step[1]} litres")
        print(f"Final State: Jug1 has {result[-1][0]} litres, Jug2 has {result[-1][1]} litres")
    else:
        print("No solution found")
