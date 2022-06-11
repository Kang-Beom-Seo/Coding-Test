N = int(input())
houses = list(map(int, input().split()))
houses.sort()
middle_left = houses[N // 2 - 1]
middle_right = houses[N // 2]
left_distance = 0
right_distance = 0
for house in houses:
    left_distance += abs(house - middle_left)
    right_distance += abs(house - middle_right)
if left_distance <= right_distance:
    print(middle_left)
else:
    print(middle_right)