from library import ints


def solve(problem):
    questions = []
    for q in range(len(problem[0])):
        correct = 0
        for p in range(len(problem)):
            correct += 1 if problem[p][q] == '1' else 0
        questions.append(correct / len(problem))

    players = [0] * len(problem)
    for p in range(len(problem)):
        for q in range(len(problem[p])):
            players[p] += 1 if problem[p][q] == '1' else 0

    anomalies = []
    for p in range(len(problem)):
        if players[p] < 0.5:
            continue
        correct, wrong = 0.0, 0.0
        for q in range(len(problem[p])):
            if problem[p][q] == '1':
                correct += questions[q]
            else:
                wrong += questions[q]
        correct /= players[p]
        wrong /= 10000 - players[p]
        anomalies.append((correct - wrong, p + 1))
    return sorted(anomalies)[0][1]


if __name__ == '__main__':
    t = ints(input())[0]
    _ = input()

    for case in range(1, t + 1):
        print(f'Case #{case}: {solve([input() for _ in range(100)])}')
