import sys
from library import ints


def send_query(x1, x2, x3):
    print(x1, x2, x3)
    sys.stdout.flush()
    return int(input())


def valid_order(x1, x2, x3):
    m = send_query(x1, x2, x3)
    if m == x1:
        return [x3, x1, x2]
    elif m == x2:
        return [x1, x2, x3]
    else:
        return [x1, x3, x2]


def find_position(po, left, right, x):
    diff = right - left + 1
    if diff == 2:
        p1, p2 = left, right
    else:
        pivot = diff // 3
        p1, p2 = left + pivot, right - pivot + 1
    order = valid_order(po[p1], po[p2], x)

    if order[0] == po[p1] and order[2] == po[p2]:
        if p2 - p1 == 1:
            return p2
        elif p2 - p1 == 2:
            return find_position(po, p1, p2 - 1, x)
        else:
            return find_position(po, p1 + 1, p2 - 1, x)
    elif order[1] == po[p1] and order[2] == po[p2]:
        if p1 - left == 0:
            return left
        elif p1 - left == 1:
            return find_position(po, left, p1, x)
        else:
            return find_position(po, left, p1 - 1, x)
    elif order[0] == po[p1] and order[1] == po[p2]:
        if right - p2 == 0:
            return right + 1
        elif right - p2 == 1:
            return find_position(po, p2, right, x)
        else:
            return find_position(po, p2 + 1, right, x)


def solve(n):
    po = valid_order(1, 2, 3)
    for nxt in range(4, n + 1):
        p = find_position(po, 0, len(po) - 1, nxt)
        po.insert(p, nxt)

    return po


if __name__ == '__main__':
    T, N, Q = ints(input())

    for case in range(1, T + 1):
        print(' '.join(map(str, solve(N))))
        correct = input()
        if correct != '1':
            exit(1)
