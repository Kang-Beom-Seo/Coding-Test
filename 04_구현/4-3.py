start = input()
x = int(start[1])
y = ord(start[0]) - ord('a') + 1
count = 0

dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]

def check_valid(nx, ny):
    return (nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8)

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if check_valid(nx, ny):
        count += 1

print(count)