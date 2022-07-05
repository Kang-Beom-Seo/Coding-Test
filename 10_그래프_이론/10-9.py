from collections import deque

N = int(input())
courses = [0] * (N + 1)
minimum_time = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for i in range(1, N + 1):
    intake = list(map(int, input().split()))
    intake.pop()
    courses[i] = intake[0]
    for c in intake[1:]:
        graph[c].append(i)
        indegree[i] += 1

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    minimum_time[now] += courses[now]
    for node in graph[now]:
        minimum_time[node] = max(minimum_time[node], minimum_time[now])
        indegree[node] -= 1
        if indegree[node] == 0:
            queue.append(node)

for i in range(1, N + 1):
    print(minimum_time[i])