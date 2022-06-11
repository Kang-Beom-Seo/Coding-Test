from collections import deque

N = int(input())
K = int(input())
isVisiting = [[0 for _ in range(N + 1)] for __ in range(N + 1)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(K):
    x, y = map(int, input().split())
    isVisiting[x][y] = 2
L = int(input())
switch_list = deque([tuple(input().split()) for _ in range(L)])
isVisiting[1][1] = 1
queue = deque([(1, 1)])
now_direction = 1
now_head = (1, 1)
now_time = 0
now_switch_time, now_switch_direction = switch_list.popleft()
now_switch_time = int(now_switch_time)

def isValid(nx, ny):
    return (nx >= 1 and nx <= N and ny >= 1 and ny <= N)

while True:
    now_time += 1
    now_x, now_y = now_head
    nx = now_x + dx[now_direction]
    ny = now_y + dy[now_direction]

    if not isValid(nx, ny) or isVisiting[nx][ny] == 1:
        break

    now_head = (nx, ny)
    queue.append(now_head)

    if isVisiting[nx][ny] == 0:
        tail_x, tail_y = queue.popleft()
        isVisiting[tail_x][tail_y] = 0

    isVisiting[nx][ny] = 1

    if now_time == now_switch_time:
        if now_switch_direction == "L":
            now_direction = (now_direction - 1) % 4
        else:
            now_direction = (now_direction + 1) % 4
        if switch_list:
            now_switch_time, now_switch_direction = switch_list.popleft()
            now_switch_time = int(now_switch_time)
print(now_time)