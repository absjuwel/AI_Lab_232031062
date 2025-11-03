
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 2},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

def dfs(start, goal):
    visited = set()
    stack = [(start, [start])]
    
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append((neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    print("DFS Path:", dfs('A', 'F'))
