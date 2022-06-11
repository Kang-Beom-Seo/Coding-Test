INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF for _ in range(n + 1)] for __ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if j == k or i == j or i == k:
                continue
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        distance = graph[i][j]
        if distance == INF:
            distance = 0
        print(distance, end=' ')
    print()