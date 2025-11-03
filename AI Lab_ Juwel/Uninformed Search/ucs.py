
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 2},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

def ucs(start, goal):
    visited = set()
    queue = [(0, start, [start])]  
    
    while queue:
        queue.sort(key=lambda x: x[0]) 
        cost, node, path = queue.pop(0)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                queue.append((cost + weight, neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    path, cost = ucs('A', 'F')
    print("UCS Path:", path, "Cost:", cost)
