INF = int(1e9)
T = int(input())

def get_smallest_node(distance, visited, N):
    minimum_dst = INF
    indexi, indexj = 1, 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not visited[i][j] and minimum_dst > distance[i][j]:
                minimum_dst = distance[i][j]
                indexi, indexj = i, j
    return indexi, indexj

def dijkstra(start, graph, distance, visited, N):
    nowx, nowy = start
    distance[nowx][nowy] = 0
    visited[nowx][nowy] = True
    while not visited[N][N]:
        for info in graph[nowx][nowy]:
            x, y, cost = info
            if distance[x][y] > distance[nowx][nowy] + cost:
                distance[x][y] = distance[nowx][nowy] + cost
        nowx, nowy = get_smallest_node(distance, visited, N)
        visited[nowx][nowy] = True

    return distance[N][N]

while T > 0:
    N = int(input())
    graph = [[[] for _ in range(N + 2)] for __ in range(N + 2)]
    distance = [[INF] * (N + 2) for _ in range(N + 2)]
    visited = [[False] * (N + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        costs = list(map(int, input().split()))
        for idx, cost in enumerate(costs):
            x, y = i, idx + 1
            graph[x - 1][y].append((x, y, cost))
            graph[x + 1][y].append((x, y, cost))
            graph[x][y - 1].append((x, y, cost))
            graph[x][y + 1].append((x, y, cost))
    answer = dijkstra((1, 1), graph, distance, visited, N) + graph[0][1][0][2]
    print(answer)

    T -= 1