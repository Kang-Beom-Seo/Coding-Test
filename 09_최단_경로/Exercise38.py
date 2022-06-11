from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
isreachable = [[False] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

def search(start):
    isreachable[start][start] = True
    visited = [False] * (N + 1)
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        if visited[node]:
            continue
        visited[node] = True
        isreachable[start][node] = True
        for a in graph[node]:
            if not visited[a]:
                q.append(a)

for i in range(1, N + 1):
    search(i)

answer = 0
for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        if isreachable[i][j] or isreachable[j][i]:
            count += 1
    if count == N:
        answer += 1
print(answer)