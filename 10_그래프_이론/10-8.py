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
parent = [i for i in range(N + 1)]
q = []

for _ in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(q, (C, A, B))

answer = 0
count = 0

while count < N - 2:
    cost, A, B = heapq.heappop(q)
    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        answer += cost
        count += 1

print(answer)