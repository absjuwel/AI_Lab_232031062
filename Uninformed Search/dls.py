graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dls(node, goal, depth, path=None, visited=None):
    if path is None:
        path = [node]
    if visited is None:
        visited = set()
    
    if node == goal:
        return path

    if depth <= 0:
        return None
    
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dls(neighbor, goal, depth - 1, path + [neighbor], visited)
            if result:
                return result
    
    visited.remove(node)
    return None


if __name__ == "__main__":

    path = dls('A', 'F', 3)
    if path:
        print(f"Path found (Depth {3}): {path}")
    else:
        print(f"No path found within depth {3}")
