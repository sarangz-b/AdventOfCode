import re

def get_val(data, pattern):
    return re.findall(pattern, data)

def p1(data):
    parsed = get_val(data, r'mul\((\d{1,3}),(\d{1,3})\)')
    return sum(int(x) * int(y) for x, y in parsed)

def p2(data):
    parsed = get_val(data, r'(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)')
    mul = True
    total = 0
    for positive, negative, v1, v2 in parsed:
        if positive:
            mul = True
        elif negative:
            mul = False
        if mul and v1 and v2:
            total += int(v1) * int(v2)
    return total

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        data = f.read()
    print('part 1:', p1(data))
    print('part 2:', p2(data))