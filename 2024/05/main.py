def p1(updates, rules):
    ans = 0
    for up in updates:
        ok = True
        for a, b in rules:
            if a in up and b in up:
                if up.index(a) > up.index(b):
                    ok = False
                    break
        if ok:
            ans += int(up[len(up) // 2])
    return ans

def p2(updates, rules):
    ans = 0
    for up in updates:
        g = {x: [] for x in up}
        deg = {x: 0 for x in up}
        for a, b in rules:
            if a in g and b in g:
                g[a].append(b)
                deg[b] += 1
        q = [x for x in up if deg[x] == 0]
        res = []
        while q:
            x = q.pop(0)
            res.append(x)
            for nei in g[x]:
                deg[nei] -= 1
                if deg[nei] == 0:
                    q.append(nei)
        if res != up:
            ans += int(res[len(res) // 2])
    return ans

if __name__ == '__main__':
    with open("./input.txt", 'r') as f:
        data1, data2 = f.read().strip().split("\n\n")
    rules = [tuple(x.split("|")) for x in data1.split("\n")]
    updates = [x.split(",") for x in data2.split("\n")]
    print('part 1:', p1(updates, rules))
    print('part 2:', p2(updates, rules))
