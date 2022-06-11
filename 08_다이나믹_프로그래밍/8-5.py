X = int(input())
DP = [-1 for _ in range(X + 1)]
DP[0] = DP[1] = 0

def get_smallest(x):
    if x == 1:
        return
    answer_list = []
    if DP[x - 1] == -1:
        get_smallest(x - 1)
    answer_list.append(DP[x - 1])
    if x % 5 == 0:
        if DP[x // 5] == -1:
            get_smallest(x // 5)
        answer_list.append(DP[x // 5])
    if x % 3 == 0:
        if DP[x // 3] == -1:
            get_smallest(x // 3)
        answer_list.append(DP[x // 3])
    if x % 2 == 0:
        if DP[x // 2] == -1:
            get_smallest(x // 2)
        answer_list.append(DP[x // 2])
    DP[x] = min(answer_list) + 1
    return

get_smallest(X)
print(DP[X])    