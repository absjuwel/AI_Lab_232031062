
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 2},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

heuristic = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0
}

def greedy_best_first(start, goal):
    visited = set()
    queue = [(heuristic[start], start, [start])]
    
    while queue:
        queue.sort(key=lambda x: x[0])
        h, node, path = queue.pop(0)
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((heuristic[neighbor], neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    print("Greedy Best-First Path:", greedy_best_first('A', 'F'))
