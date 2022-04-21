N = int(input())
plan = input().split()
x = 1
y = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direction_dict = {'L' : 0, 'R' : 1, 'U' : 2, 'D' : 3}

def check_valid(next_x, next_y):
    return (next_x >= 1 and next_x <= N and next_y >= 1 and next_y <= N)

for d in plan:
    next_x = x + dx[direction_dict[d]]
    next_y = y + dy[direction_dict[d]]
    if check_valid(next_x, next_y):
        x = next_x
        y = next_y

print(f"{x} {y}")