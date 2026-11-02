import random

def calculate_cost(state):
    n = len(state)
    cost = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                cost += 1
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost

def get_best_neighbor(state):
    n = len(state)
    current_cost = calculate_cost(state)
    best_state = list(state)
    best_cost = current_cost

    for col in range(n):
        for row in range(n):
            if state[col] != row:
                neighbor = list(state)
                neighbor[col] = row
                neighbor_cost = calculate_cost(neighbor)
                
                if neighbor_cost < best_cost:
                    best_cost = neighbor_cost
                    best_state = neighbor
                    
    return best_state, best_cost

def hill_climbing_8_queens():
    restarts = 0
    while True:
        current_state = [random.randint(0, 7) for _ in range(8)]
        step = 0
        
        while True:
            current_cost = calculate_cost(current_state)
            
            if current_cost == 0:
                print(f"Goal state reached with {restarts} restart(s)!")
                return current_state
                
            neighbor_state, neighbor_cost = get_best_neighbor(current_state)
            
            if neighbor_cost >= current_cost:
                restarts += 1
                break
                
            current_state = neighbor_state
            step += 1

def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)

if __name__ == "__main__":
    solution = hill_climbing_8_queens()
    print("\nSolution State:", solution)
    print("Cost:", calculate_cost(solution))
    print("\n8-Queens Board:")
    print_board(solution)
    print()
    print("SHRIHARI SUDHAKAR BADIGER: 1BM25CS522")