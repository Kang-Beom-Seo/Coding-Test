N, M = list(map(int, input().split()))
MAXIMUM = 987654321
coins = [int(input()) for _ in range(N)]
memo = [MAXIMUM for _ in range(M + 1)]
for coin in coins:
    if coin <= M:
        memo[coin] = 1
for i in range(M):
    for coin in coins:
        if i + coin <= M:
            memo[i + coin] = min(memo[i] + 1, memo[i + coin])
if memo[M] == MAXIMUM:
    print(-1)
else:
    print(memo[M])