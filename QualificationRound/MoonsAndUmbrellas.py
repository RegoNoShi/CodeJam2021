import re
from library import ints


def cost(x, y, s):
    prev = None
    count = 0
    for c in s:
        if prev == 'C' and c == 'J':
            count += x
        elif prev == 'J' and c == 'C':
            count += y
        prev = c
    return count


def solve(x, y, s):
    if len(s) <= 1:
        return 0

    while True:
        matches = list(re.finditer(r'((?:^|C|J)\?+(?:$|C|J))', s))
        if len(matches) == 0:
            break
        f = list(s)
        for m in matches:
            f[m.start():m.end()] = maximize_swaps(x, y, m.group()) if x + y < 0 else minimize_swaps(x, y, m.group())
        s = ''.join(f)
    return cost(x, y, s)


def maximize_swaps(x, y, s):
    mc = (float('inf'), None)
    qm = s.count('?')
    regexp = r'\?' * qm
    options = ['CJ' * (qm // 2), 'JC' * (qm // 2)] if qm % 2 == 0 else \
        ['CJ' * (qm // 2) + 'C', 'JC' * (qm // 2) + 'J', 'CJ' * (qm // 2) + 'J', 'JC' * (qm // 2) + 'C']

    for opt in options:
        sm = re.sub(regexp, opt, s)
        cst = cost(x, y, sm)
        if cst < mc[0]:
            mc = (cst, sm)
    return mc[1]


def minimize_swaps(x, y, s):
    mc = (float('inf'), None)
    qm = s.count('?')
    regexp = r'\?' * qm
    options = ['J' + 'C' * (qm - 1), 'C' + 'J' * (qm - 1), 'C' * qm, 'J' * qm]

    for opt in options:
        sm = re.sub(regexp, opt, s)
        cst = cost(x, y, sm)
        if cst < mc[0]:
            mc = (cst, sm)
    return mc[1]


if __name__ == '__main__':
    T = ints(input())[0]

    for case in range(1, T + 1):
        line = input()
        X, Y = ints(line)
        S = line.split()[-1]
        print(f'Case #{case}: {solve(X, Y, S)}')
