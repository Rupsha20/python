def build_graph():
    graph = {}
    for i in range(int(input("Number of nodes: "))):
        node = input("Node: ")
        graph[node] = input(f"Neighbors of {node}: ").split()
    return graph

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    g = build_graph()
    start_node = input("Start node: ")
    print("\nDFS Traversal:")
    dfs(g, start_node)
