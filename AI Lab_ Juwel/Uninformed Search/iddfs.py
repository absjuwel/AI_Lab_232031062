
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 2},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

def dls(node, goal, depth, path, visited):
    if depth == 0 and node == goal:
        return path
    if depth > 0:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                result = dls(neighbor, goal, depth-1, path + [neighbor], visited)
                if result:
                    return result
        visited.remove(node)
    return None

def iddfs(start, goal, max_depth=10):
    for depth in range(max_depth):
        visited = set()
        result = dls(start, goal, depth, [start], visited)
        if result:
            return result
    return None

if __name__ == "__main__":
    print("IDDFS Path:", iddfs('A', 'F'))
