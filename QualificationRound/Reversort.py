from library import ints


def solve(problem):
    cost = 0
    for i in range(len(problem) - 1):
        j = problem.index(min(problem[i:]))
        cost += j - i + 1
        problem[i:j + 1] = list(reversed(problem[i:j + 1]))
    return cost


if __name__ == '__main__':
    t = int(input())

    for case in range(1, t + 1):
        _ = input()
        print(f'Case #{case}: {solve(ints(input()))}')
