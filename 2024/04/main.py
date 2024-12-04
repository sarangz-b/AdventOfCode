def get_val(grid, x, y, dx, dy, target):
    for k in range(len(target)):
        nx, ny = x + dx * k, y + dy * k
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != target[k]:
            return False
    return True


def p1(data):
    word = "XMAS"
    d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            for dr, dc in d:
                if get_val(data, row, col, dr, dc, word):
                    count += 1
    return count

def cross_mas(g, r, c):
    pat = [
        [(-1, -1, 'M'), (-1, 1, 'S'), (1, -1, 'M'), (1, 1, 'S')],
        [(-1, -1, 'S'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'M')],
        [(-1, -1, 'M'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'S')],
        [(-1, -1, 'S'), (-1, 1, 'S'), (1, -1, 'M'), (1, 1, 'M')],
    ]
    for p in pat:
        if all(
            0 <= r + dr < len(g) and 0 <= c + dc < len(g[0]) and g[r + dr][c + dc] == char
            for dr, dc, char in p
        ):
            return True
    return False
def p2(data):
    count = 0
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == 'A' and cross_mas(data, r, c):
                count += 1
    return count

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        data = f.read().split("\n")

    print('part 1:', p1(data))
    print('part 2:', p2(data))