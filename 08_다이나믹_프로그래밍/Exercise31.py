T = int(input())

while T > 0:
    n, m = map(int, input().split())
    gold_mine = [[0 for _ in range(m + 2)] for __ in range(n + 2)]
    memo = [[0 for _ in range(m + 2)] for __ in range(n + 2)]
    golds = list(map(int, input().split()))
    for idx, gold in enumerate(golds):
        gold_mine[idx // m + 1][idx % m + 1] = gold
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            memo[j][i] = max(memo[j - 1][i - 1], memo[j][i - 1], memo[j + 1][i - 1]) + gold_mine[j][i]
    print(max([memo[i][m] for i in range(1, n + 1)]))

    T -= 1