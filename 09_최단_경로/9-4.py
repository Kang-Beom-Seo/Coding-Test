INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    graph[i][i] = 0
for i in range(M):
    c1, c2 = map(int, input().split())
    graph[c1][c2] = 1
    graph[c2][c1] = 1
X, K = map(int, input().split())

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = graph[1][K] + graph[K][X]
if answer >= INF:
    answer = -1
print(answer)