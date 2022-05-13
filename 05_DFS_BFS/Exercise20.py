import copy


N = int(input())
corridor = [[something for something in input().split()] for _ in range(N)]
number_of_cases = []
teachers_position = [(i, j) for i in range(N) for j in range(N) if corridor[i][j] == "T"]

def get_O_number_of_cases(now_cases, position, num):
    if num == 3:
        number_of_cases.append(now_cases)
        return
    for i in range(position + 1, N * N):
        if corridor[i // N][i % N] == 'X':
            next_cases = copy.deepcopy(now_cases)
            next_cases.append((i // N, i % N))
            get_O_number_of_cases(next_cases, i, num + 1)
    return

def isDetected(corridor_map, teacher_position):
    dx = [-1, 1]
    dy = [-1, 1]
    for d in dx:
        now_x, now_y = teacher_position
        while isValid(now_x, now_y):
            if corridor_map[now_x][now_y] == "O":
                break
            elif corridor_map[now_x][now_y] == "S":
                return True
            now_x += d
    
    for d in dy:
        now_x, now_y = teacher_position
        while isValid(now_x, now_y):
            if corridor_map[now_x][now_y] == "O":
                break
            elif corridor_map[now_x][now_y] == "S":
                return True
            now_y += d
    
    return False

def isValid(nx, ny):
    return (nx >= 0 and nx < N and ny >= 0 and ny < N)


get_O_number_of_cases([], -1, 0)
for O_case in number_of_cases:
    detected = False
    simulation_corridor = copy.deepcopy(corridor)
    for O_x, O_y in O_case:
        simulation_corridor[O_x][O_y] = "O"
    for teacher_position in teachers_position:
        if isDetected(simulation_corridor, teacher_position):
            detected = True
            break
    if not detected:
        break

if detected:
    print("NO")
else:
    print("YES")