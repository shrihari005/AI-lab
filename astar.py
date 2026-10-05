import heapq

INITIAL = ((2, 8, 3),
           (1, 6, 4),
           (0, 7, 5))

GOAL = ((1, 2, 3),
        (8, 0, 4),
        (7, 6, 5))

COUNT_BLANK = False


def h(state):
    """Heuristic: number of misplaced tiles."""
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != GOAL[i][j]:
                if state[i][j] == 0 and not COUNT_BLANK:
                    continue
                count += 1
    return count


def neighbors(state):
    """Generate all states reachable by sliding one tile into the blank."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                bi, bj = i, j
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = bi + di, bj + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            board = [list(r) for r in state]
            board[bi][bj], board[ni][nj] = board[ni][nj], board[bi][bj]
            yield tuple(tuple(r) for r in board)


def a_star(start, goal):
    counter = 0 
    open_list = [(h(start), counter, 0, start)]
    parent = {start: None}
    best_g = {start: 0}
    closed = set()

    while open_list:
        f, _, g, state = heapq.heappop(open_list)
        if state in closed:
            continue
        closed.add(state)

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1], len(closed)

        for nxt in neighbors(state):
            new_g = g + 1 
            if nxt not in best_g or new_g < best_g[nxt]:
                best_g[nxt] = new_g
                parent[nxt] = state
                counter += 1
                heapq.heappush(open_list, (new_g + h(nxt), counter, new_g, nxt))
    return None, len(closed)


def show(state, g):
    print(f"g(n) = {g}, h(n) = {h(state)}, f(n) = {g + h(state)}")
    for row in state:
        print(" ".join(str(x) if x else "_" for x in row))
    print()


if __name__ == "__main__":
    path, expanded = a_star(INITIAL, GOAL)
    if path is None:
        print("No solution found.")
    else:
        for step, state in enumerate(path):
            print(f"Step {step}")
            show(state, step)
        print(f"Solution cost (moves): {len(path) - 1}")
        print(f"Nodes expanded: {expanded}")
