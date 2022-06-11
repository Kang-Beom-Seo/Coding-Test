N = int(input())
soldiers = list(map(int, input().split()))
memo = [1 for _ in range(N)]
for i in range(1, N):
    for j in range(i):
        if soldiers[j] > soldiers[i]:
            memo[i] = max(memo[i], memo[j] + 1)
print(N - max(memo))