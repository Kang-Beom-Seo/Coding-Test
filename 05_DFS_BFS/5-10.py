N, M = map(int, input().split())
ice_map = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
for i in range(N):
    row = input()
    for j in range(M):
        ice_map[i][j] = ord(row[j]) - ord('0')

def check_valid(node):
    i, j = node
    return (i >= 0 and i < N and j >= 0 and j < M)

def dfs(graph, visited, node):
    x, y = node
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if check_valid((nx, ny)):
            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                dfs(graph, visited, (nx, ny))

for i in range(N):
    for j in range(M):
        if ice_map[i][j] == 0 and visited[i][j] == 0:
            dfs(ice_map, visited, (i, j))
            result += 1

print(result)