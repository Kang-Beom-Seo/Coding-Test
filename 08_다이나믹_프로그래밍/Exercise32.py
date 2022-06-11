n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
memo = [[0 for _ in range(i)] for i in range(1, n + 1)]
memo[0][0] = triangle[0][0]
for i in range(n - 1):
    for j in range(i + 1):
        memo[i + 1][j] = max(memo[i + 1][j], memo[i][j] + triangle[i + 1][j])
        memo[i + 1][j + 1] = max(memo[i + 1][j + 1], memo[i][j] + triangle[i + 1][j + 1])
print(max(memo[-1]))