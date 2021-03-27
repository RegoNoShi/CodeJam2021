from library import ints


def solve(n, c):
    if c < n - 1 or c > (n * (n + 1) // 2 - 1):
        return 'IMPOSSIBLE'

    r = list(range(1, n + 1))
    c -= n - 1
    start, end = 0, n - 1
    swaps = 0
    while c > 0:
        if end - start <= c:
            r[start:end + 1] = list(reversed(r[start:end + 1]))
            c -= end - start
        if swaps % 2 == 0:
            end -= 1
        else:
            start += 1
        swaps += 1

    return ' '.join(map(str, r))


if __name__ == '__main__':
    t = ints(input())[0]

    for case in range(1, t + 1):
        N, C = ints(input())
        print(f'Case #{case}: {solve(N, C)}')
