N = input()
length = len(N)
left = N[:length // 2]
right = N[length // 2:]
left_sum = right_sum = 0
for left_num in left:
    left_sum += int(left_num)
for right_num in right:
    right_sum += int(right_num)
if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")