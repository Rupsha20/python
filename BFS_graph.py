import queue

def graph():
    graph = {}
    for i in range(int(input("Number of nodes: "))):
        node = input("Node: ")
        graph[node] = input(f"Neighbors of {node}: ").split()
    return graph

# BFS algorithm
def bfs(graph, start_node):
    visited = set()
    q = queue.Queue()
    q.put(start_node)         # put means  Adds an item to the queue.
    
    while not q.empty():
        node = q.get()       # get means Removes and returns an item from the queue.
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor in graph[node]:
                if neighbor not in visited:
                    q.put(neighbor)

if __name__ == "__main__":
    g = graph()
    start_node = input("Start node: ")
    print("\nBFS Traversal:")
    bfs(g, start_node)
