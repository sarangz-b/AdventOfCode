def check(data):
    value_d = data[1] - data[0]
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        if diff * value_d <= 0 or abs(diff) > 3:
            return False
    return True

def check_with_dampener(data):
    for i in range(len(data)):
        mod = data[:i] + data[i+1:]
        if check(mod):
            return True
    return False

def main():
    with open('./input.txt', 'r') as f:
        data = f.readlines()
    values = [list(map(int, line.split())) for line in data]
    check_part1 = sum(check(val) for val in values)
    check_part2 = sum(check_with_dampener(val) for val in values)
    print("Part 1:", check_part1)
    print("Part 2:", check_part2)

if __name__ == "__main__":
    main()