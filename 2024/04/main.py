def check_window(window, center_val, dirs=None, pats=None):
    mid = len(window) // 2
    if window[mid][mid] != center_val:
        return False
    count = 0
    if dirs:
        word = [ 'M', 'A', 'S']
        for d in dirs:
            if all(
                0 <= mid + dx < len(window) and
                0 <= mid + dy < len(window[0]) and
                window[mid + dx][mid + dy] == word[i]
                for i, (dx, dy) in enumerate(d)
            ):
                count += 1
    if pats:
        for p in pats:
            if all(
                0 <= mid + dr < len(window) and
                0 <= mid + dc < len(window[0]) and
                window[mid + dr][mid + dc] == char
                for dr, dc, char in p
            ):
                count += 1
    return count

def p1(data):
    dirs = [
        [(0, 1), (0, 2), (0, 3)],
        [(0, -1), (0, -2), (0, -3)],
        [(1, 0), (2, 0), (3, 0)],
        [(-1, 0), (-2, 0), (-3, 0)],
        [(1, 1), (2, 2), (3, 3)],
        [(-1, -1), (-2, -2), (-3, -3)],
        [(1, -1), (2, -2), (3, -3)],
        [(-1, 1), (-2, 2), (-3, 3)]
    ]
    count = 0
    size = 7
    for r in range(len(data) - size + 1):
        for c in range(len(data[r]) - size + 1):
            window = [row[c:c + size] for row in data[r:r + size]]
            count += check_window(window, 'X', dirs)
    return count

def p2(data):
    pats = [
        [(-1, -1, 'M'), (-1, 1, 'S'), (1, -1, 'M'), (1, 1, 'S')],
        [(-1, -1, 'S'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'M')],
        [(-1, -1, 'M'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'S')],
        [(-1, -1, 'S'), (-1, 1, 'S'), (1, -1, 'M'), (1, 1, 'M')],
    ]
    count = 0
    size = 3
    for r in range(len(data) - size + 1):
        for c in range(len(data[r]) - size + 1):
            window = [row[c:c + size] for row in data[r:r + size]]
            count += check_window(window, 'A', pats=pats)
    return count

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        data = f.read().split("\n")

    print('part 1:', p1(data))
    print('part 2:', p2(data))