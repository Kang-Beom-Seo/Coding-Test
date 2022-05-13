import sys

sys.setrecursionlimit(10**5)
N, L, R = map(int, input().split())
country = [[population for population in map(int, input().split())] for _ in range(N)]

def get_union(now_position, visited, union_list):
    x, y = now_position
    visited[x][y] = True
    union_list.append(now_position)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if isValid(nx, ny) and not visited[nx][ny] and isUnion(x, y, nx, ny):
            get_union((nx, ny), visited, union_list)
    return

def isValid(nx, ny):
    return (nx >= 0 and nx < N and ny >= 0 and ny < N)

def isUnion(x, y, nx, ny):
    difference = abs(country[x][y] - country[nx][ny])
    return (difference >= L and difference <= R)

count = 0
while True:
    visited = [[False for _ in range(N)] for __ in range(N)]
    unions_list = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union_list = []
                get_union((i, j), visited, union_list)
                unions_list.append(union_list)
    if len(unions_list) == N * N:
        break
    for union in unions_list:
        if len(union) > 1:
            total = 0
            total_length = len(union)
            for union_member in union:
                member_x, member_y = union_member
                total += country[member_x][member_y]
            for union_member in union:
                member_x, member_y = union_member
                country[member_x][member_y] = total // total_length
    count += 1
print(count)