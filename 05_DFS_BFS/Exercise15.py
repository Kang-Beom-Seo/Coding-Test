import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
cities = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for _ in range(M):
    c1, c2 = map(int, sys.stdin.readline().split())
    cities[c1].append(c2)

def bfs(graph, visited, node):
    distance = 0
    visited[node] = True
    answers = []
    queue = deque()
    queue.append((node, distance))
    while queue:
        node, distance = queue.popleft()
        if distance == K:
            answers.append(node)
            continue
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, distance + 1))
    
    return answers

answers = bfs(cities, visited, X)
if not answers:
    print(-1)
else:
    answers.sort()
    for answer in answers:
        print(answer)