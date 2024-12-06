def path(grid, start, dir):
    memory_pos = set()
    cur_pos = start
    dir_idx = 0
    while True:
        memory_pos.add(cur_pos)
        next_pos = (cur_pos[0] + dir[dir_idx][0], cur_pos[1] + dir[dir_idx][1])
        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
            break
        if grid[next_pos[0]][next_pos[1]] == "#":
            dir_idx = (dir_idx + 1) % 4
        else:
            cur_pos = next_pos
    return memory_pos

def initiate(grid, start, dir, obst):
    cur_pos = start
    dir_idx = 0
    visited_states = set()
    grid[obst[0]][obst[1]] = "#"

    while True:
        state = (cur_pos, dir_idx)
        if state in visited_states:
            grid[obst[0]][obst[1]] = "."
            return True
        visited_states.add(state)
        next_pos = (cur_pos[0] + dir[dir_idx][0], cur_pos[1] + dir[dir_idx][1])

        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
            grid[obst[0]][obst[1]] = "."
            return False

        if grid[next_pos[0]][next_pos[1]] == "#":
            dir_idx = (dir_idx + 1) % 4
        else:
            cur_pos = next_pos

def p1(data):
    grid = [list(row) for row in data]
    start_pos = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "^":
                start_pos = (r, c)
                break
        if start_pos:
            break

    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = path(grid, start_pos, dir)
    return len(visited)

def p2(data):
    grid = [list(row) for row in data]
    start_pos = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "^":
                start_pos = (r, c)
                break
        if start_pos:
            break

    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    obst = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "." and (r, c) != start_pos:
                if initiate(grid, start_pos, dir, (r, c)):
                    obst += 1

    return obst

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        data = f.read().splitlines()

    print('part 1:', p1(data))
    print('part 2:', p2(data))
