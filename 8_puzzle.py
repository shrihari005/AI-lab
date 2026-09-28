def dfs(state, goal, visited, limit=15):
    if state == goal:
        return [state]
    if limit == 0:
        return None
    
    visited.add(state)
    zero_idx = state.index(0)
    row, col = divmod(zero_idx, 3)

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_zero_idx = r * 3 + c
   
            lst = list(state)
            lst[zero_idx], lst[new_zero_idx] = lst[new_zero_idx], lst[zero_idx]
            next_state = tuple(lst)
            
            if next_state not in visited:
                result = dfs(next_state, goal, visited, limit - 1)
                if result:
                    return [state] + result
                    
    visited.remove(state)
    return None

start_state = (1, 2, 3, 
               0, 4, 6, 
               7, 5, 8)
goal_state  = (1, 2, 3, 
               4, 5, 6, 
               7, 8, 0)

path = dfs(start_state, goal_state, set())

if path:
    print("Path found: True")
    print(f"Path cost (number of moves): {len(path) - 1}")
else:
    print("Path found: False")

print("Shrihari Sudhakar Badiger: 1BM25CS522")
