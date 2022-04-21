N, M = map(int, input().split())
x, y, direction = map(int, input().split())
game_map = []
visited = []
for i in range(N):
    row = list(map(int, input().split()))
    visited.append([0 for _ in range(M)])
    game_map.append(row)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 1
impossible = 0

def turn_left(now_direction):
    return (now_direction - 1) % 4

def turn_back(now_direction):
    return (now_direction - 2) % 4

def check_valid(nx, ny, isBack):
    if nx < 0 or nx > N or ny < 0 or ny > M:
        return False
    if isBack:
        if game_map[nx][ny] == 1:
            return False
        else:
            return True
    else:
        if game_map[nx][ny] == 1 or visited[nx][ny] == 1:
            return False
        else:
            return True

while True:
    visited[x][y] = 1
    if impossible == 4:
        nd = turn_back(direction)
        nx = x + dx[nd]
        ny = y + dy[nd]
        if check_valid(nx, ny, True):
            x = nx
            y = ny
            impossible = 0
            continue
        else:
            break
        
    nd = turn_left(direction)
    nx = x + dx[nd]
    ny = y + dy[nd]
    if check_valid(nx, ny, False):
        x = nx
        y = ny
        impossible = 0
        count += 1
    else:
        impossible += 1
        
    direction = nd

print(count)