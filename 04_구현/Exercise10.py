def turn_right(key):
    new_key = []
    height = len(key)
    width = height
    for i in range(width):
        row = []
        for j in range(height - 1, -1, -1):
            row.append(key[j][i])
        new_key.append(row)
    return new_key

def key_lock_match(i, j, width_shift, height_shift, M):
    return (i >= height_shift and i < M + height_shift and j >= width_shift and j < M + width_shift)

def solution(key, lock):
    M = len(key)
    N = len(lock)
    for i in range(4):
        key = turn_right(key)
        for width_shift in range(-N, N):
            for height_shift in range(-N, N):
                not_answer = False
                for i in range(N):
                    for j in range(N):
                        isMatch = key_lock_match(i, j, width_shift, height_shift, M)
                        if not isMatch:
                            if lock[i][j] == 0:
                                not_answer = True
                                break
                        else:
                            if lock[i][j] ^ key[i - height_shift][j - width_shift] == 0:
                                not_answer = True
                                break
                    if not_answer:
                        break
                if not not_answer:
                    return True
    
    return False