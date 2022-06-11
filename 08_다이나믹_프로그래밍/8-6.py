N = int(input())
K = list(map(int, input().split()))

memo = [0 for _ in range(N + 1)]
memo[0] = K[0]
memo[1] = max(K[0], K[1])
for i in range(2, N):
    memo[i] = max(memo[i - 2] + K[i], memo[i - 1])
print(memo[N - 1])