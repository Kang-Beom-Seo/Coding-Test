import heapq

INF = int(1e9)
N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
cities = []
for i in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, city = heapq.heappop(q)
        if distance[city] < dist:
            continue
        cities.append((city, dist))
        for y, z in graph[city]:
            if distance[y] > distance[city] + z:
                distance[y] = distance[city] + z
                heapq.heappush(q, (distance[y], y))
    return

dijkstra(C)
print(len(cities) - 1, cities[-1][1])