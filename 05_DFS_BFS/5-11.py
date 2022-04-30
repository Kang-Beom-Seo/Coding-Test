from collections import deque
N, M = map(int, input().split())
miro = []
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    miro.append(list(map(int, input())))

def check_valid(node):
    x, y = node
    return (x >= 0 and x < N and y >= 0 and y < M)

def bfs(graph, visited, node):
    x, y = node
    distance = 0
    visited[x][y] = True
    queue = deque()
    queue.append((x, y, distance + 1))
    while queue:
        x, y, distance = queue.popleft()
        if x == N - 1 and y == M - 1:
            return distance
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check_valid((nx, ny)):
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    queue.append((nx, ny, distance + 1))
    
    return -1

print(bfs(miro, visited, (0, 0)))