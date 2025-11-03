import random

def hill_climbing(problem, iterations=1000):

    current = problem['start']()
    current_value = problem['evaluate'](current)
    
    for _ in range(iterations):
        neighbors = problem['neighbors'](current)
        if not neighbors:
            break
        

        next_node = max(neighbors, key=problem['evaluate'])
        next_value = problem['evaluate'](next_node)
        
        if next_value <= current_value:
            break
        
        current, current_value = next_node, next_value
    
    return current, current_value



def start():
    return random.uniform(-10, 10)

def neighbors(x):
    step = 0.1
    return [x + step, x - step]

def evaluate(x):
    return -(x-3)**2 + 10

problem = {
    'start': start,
    'neighbors': neighbors,
    'evaluate': evaluate
}

if __name__ == "__main__":
    solution, value = hill_climbing(problem, iterations=1000)
    print("Best solution:", solution)
    print("Value at solution:", value)
