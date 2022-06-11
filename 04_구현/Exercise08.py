S = input()
alpha_list = []
sum = 0
for s in S:
    if s.isalpha():
        alpha_list.append(s)
    else:
        sum += int(s)
alpha_list.sort()
alpha = ''.join(alpha_list)
answer = alpha + str(sum)
print(answer)