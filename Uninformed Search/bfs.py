from collections import deque


graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 2},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

def bfs(start, goal):
    visited = set()
    queue = deque([(start, [start])])
    
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    print("BFS Path:", bfs('A', 'F'))
