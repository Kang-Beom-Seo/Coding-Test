N = int(input())
A = [i for i in map(int, input().split())]
operands_list = map(int, input().split())
answer_list = []

def DFS(A, now_value, position, operands):
    if position == N:
        answer_list.append(now_value)
        return
    add_num, subtract_num, mul_num, div_num = operands
    if add_num > 0:
        next_value = now_value + A[position]
        next_operands = (add_num - 1, subtract_num, mul_num, div_num)
        DFS(A, next_value, position + 1, next_operands)
    if subtract_num > 0:
        next_value = now_value - A[position]
        next_operands = (add_num, subtract_num - 1, mul_num, div_num)
        DFS(A, next_value, position + 1, next_operands)
    if mul_num > 0:
        next_value = now_value * A[position]
        next_operands = (add_num, subtract_num, mul_num - 1, div_num)
        DFS(A, next_value, position + 1, next_operands)
    if div_num > 0:
        if now_value < 0:
            next_value = -now_value // A[position]
            next_value = -next_value
        else:
            next_value = now_value // A[position]
        next_operands = (add_num, subtract_num, mul_num, div_num - 1)
        DFS(A, next_value, position + 1, next_operands)
    return

DFS(A, A[0], 1, operands_list)
print(max(answer_list))
print(min(answer_list))