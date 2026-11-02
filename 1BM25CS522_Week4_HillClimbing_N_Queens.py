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

def get_neighbors_by_swapping(state):
    n = len(state)
    neighbors = []
    for i in range(n):
        for j in range(i + 1, n):
            neighbor = list(state)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append((i, j, neighbor))
    return neighbors

def hill_climbing_4_queens(initial_state):
    current_state = list(initial_state)
    current_cost = calculate_cost(current_state)
    
    print(f"Initial State: {current_state} | Cost: {current_cost}\n")
    step = 0
    
    while True:
        if current_cost == 0:
            print(f"Goal state reached in {step} step(s)!")
            return current_state, True
            
        step += 1
        neighbors = get_neighbors_by_swapping(current_state)
        
        best_neighbor = None
        best_cost = float('inf')
        best_swap = None
        
        print(f"--- Iteration {step} ---")
        for i, j, neighbor in neighbors:
            cost = calculate_cost(neighbor)
            print(f"Swap (x{i}, x{j}) -> State: {neighbor} | Cost: {cost}")
            
            if cost < best_cost:
                best_cost = cost
                best_neighbor = neighbor
                best_swap = (i, j)
                
        if best_cost >= current_cost:
            print(f"\nTerminated at local minimum/shoulder. State: {current_state} | Cost: {current_cost}")
            return current_state, False
            
        current_state = best_neighbor
        current_cost = best_cost
        print(f"\nChosen Swap: {best_swap} -> New State: {current_state} | Cost: {current_cost}\n")

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
    initial_config = [3, 1, 2, 0]
    solution, success = hill_climbing_4_queens(initial_config)
    print("\nFinal Chessboard Configuration:")
    print_board(solution)
    print()
    print("SHRIHARI SUDHAKAR BADIGER: 1BM25CS522")