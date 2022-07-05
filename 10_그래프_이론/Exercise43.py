import heapq

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [i for i in range(N)]
graph_queue = []
total = 0
decreased = 0

for _ in range(M):
    X, Y, Z = map(int, input().split())
    total += Z
    heapq.heappush(graph_queue, (Z, X, Y))

while graph_queue:
    cost, X, Y = heapq.heappop(graph_queue)
    if find_parent(parent, X) != find_parent(parent, Y):
        union_parent(parent, X, Y)
        decreased += cost

print(total - decreased)