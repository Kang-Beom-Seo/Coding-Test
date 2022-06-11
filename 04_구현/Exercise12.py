def check_insert(x, y, a, column_map, beam_map):
    if a == 0:
        if y == 0:
            return True
        else:
            if column_map[x][y - 1] == 1:
                return True
            elif beam_map[x][y] == 1:
                return True
            elif x > 0 and beam_map[x - 1][y] == 1:
                return True
            else:
                return False
    else:
        if column_map[x][y - 1] == 1 or column_map[x + 1][y - 1] == 1:
            return True
        else:
            if x > 0 and beam_map[x - 1][y] == 1 and beam_map[x + 1][y] == 1:
                return True
            else:
                return False

def check_delete(column_map, beam_map):
    n = len(column_map) - 1
    for i in range(n):
        for j in range(n):
            if column_map[i][j] == 1:
                if not check_insert(i, j, 0, column_map, beam_map):
                    return False
            if beam_map[i][j] == 1:
                if not check_insert(i, j, 1, column_map, beam_map):
                    return False
    return True

def solution(n, build_frame):
    column_map = [[0 for i in range(n + 2)] for j in range(n + 2)]
    beam_map = [[0 for i in range(n + 2)] for j in range(n + 2)]
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:
            if check_insert(x, y, a, column_map, beam_map):
                if a == 0:
                    column_map[x][y] = 1
                else:
                    beam_map[x][y] = 1
        else:
            if a == 0:
                column_map[x][y] = 0
            else:
                beam_map[x][y] = 0
            if not check_delete(column_map, beam_map):
                if a == 0:
                    column_map[x][y] = 1
                else:
                    beam_map[x][y] = 1
                    
    answer = [[i, j, 0] for i in range(n + 1) for j in range(n + 1) if column_map[i][j] == 1]
    answer.extend([[i, j, 1] for i in range(n + 1) for j in range(n + 1) if beam_map[i][j] == 1])
    answer.sort(key=lambda x:(x[0], x[1], x[2]))
    
    return answer