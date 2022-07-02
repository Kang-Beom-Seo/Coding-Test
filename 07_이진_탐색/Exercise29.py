N, C = map(int, input().split())
routers = [int(input()) for _ in range(N)]
routers.sort()
MAX = routers[-1] - routers[0]

def install_available(array, target, distance):
    cnt = 1
    prev_point = array[0]
    for house in array:
        if house - prev_point >= distance:
            cnt += 1
            prev_point = house
            if cnt == target:
                return True
    return False

def binary_search(array, target, start, end):
    answer = 1
    while start <= end:
        mid = (start + end) // 2
        result = install_available(array, target, mid)
        if result:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer

answer = binary_search(routers, C, 1, MAX)
print(answer)