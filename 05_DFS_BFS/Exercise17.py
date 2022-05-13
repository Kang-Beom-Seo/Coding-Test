from collections import deque

N, K = map(int, input().split())
virus_map = [[i for i in map(int, input().split())] for _ in range(N)]
S, X, Y = map(int, input().split())

def isValid(nx, ny, N):
    return (nx >= 0 and nx < N and ny >= 0 and ny < N)

def BFS(virus_map, N, K, S):
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(1, K + 1):
        for j in range(N):
            for k in range(N):
                if virus_map[j][k] == i:
                    queue.append((i, j, k, 0))
    while queue:
        V, x, y, s = queue.popleft()
        if s >= S:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isValid(nx, ny, N) and virus_map[nx][ny] == 0:
                virus_map[nx][ny] = V
                queue.append((V, nx, ny, s + 1))
    return

BFS(virus_map, N, K, S)
print(virus_map[X - 1][Y - 1])