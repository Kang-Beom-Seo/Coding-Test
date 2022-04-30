import sys
import copy

N, M = map(int, sys.stdin.readline().split())
laboratory = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
for i in range(N):
    laboratory.append(list(map(int, sys.stdin.readline().split())))

def check_valid(node):
    x, y = node
    return (x >= 0 and x < N and y >= 0 and y < M)

def dfs(graph, visited, node):
    x, y = node
    visited[x][y] = True
    graph[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if check_valid((nx, ny)):
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                dfs(graph, visited, (nx, ny))

total = N * M
for i in range(total):
    first_wall = (i // M, i % M)
    if laboratory[first_wall[0]][first_wall[1]] != 0:
        continue
    for j in range(i + 1, total):
        second_wall = (j // M, j % M)
        if laboratory[second_wall[0]][second_wall[1]] != 0:
            continue
        for k in range(j + 1, total):
            third_wall = (k // M, k % M)
            if laboratory[third_wall[0]][third_wall[1]] != 0:
                continue
            
            laboratory_simulation = copy.deepcopy(laboratory)
            laboratory_simulation[first_wall[0]][first_wall[1]] = 1
            laboratory_simulation[second_wall[0]][second_wall[1]] = 1
            laboratory_simulation[third_wall[0]][third_wall[1]] = 1
            visited = [[False for _ in range(M)] for _ in range(N)]
            safe_area = 0
            
            for x in range(N):
                for y in range(M):
                    if laboratory_simulation[x][y] == 2 and not visited[x][y]:
                        dfs(laboratory_simulation, visited, (x, y))
            
            for x in range(N):
                for y in range(M):
                    if laboratory_simulation[x][y] == 0:
                        safe_area += 1
            
            if safe_area > result:
                result = safe_area
print(result)