N = int(input())
TP = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
TP = [elem for elem in zip(*TP)]
memo = [0 for _ in range(N + 2)]
T, P = TP
for i in range(1, N + 2):
    max_possibles = []
    for j in range(1, i):
        if j + T[j] <= i:
            max_possibles.append(memo[j] + P[j])
    if max_possibles:
        memo[i] = max(max_possibles)
print(memo[N + 1])