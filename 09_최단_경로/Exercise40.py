import heapq

INF = int(1e9)
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
distance[0] = 0
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append((B, 1))
    graph[B].append((A, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next_node, d in graph[node]:
            cost = distance[node] + d
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return

dijkstra(1)
maximum = max(distance)
answer = (distance.index(maximum), maximum, distance.count(maximum))
print(answer[0], answer[1], answer[2])