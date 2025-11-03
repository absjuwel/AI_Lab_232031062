
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

def a_star(start, goal):
    queue = [(heuristic[start], 0, start, [start])]  
    visited = set()
    
    while queue:
        queue.sort(key=lambda x: x[0])
        f, g, node, path = queue.pop(0)
        if node == goal:
            return path, g
        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node].items():
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                queue.append((f_new, g_new, neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    path, cost = a_star('A', 'F')
    print("A* Path:", path, "Cost:", cost)
