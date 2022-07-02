import sys

input = sys.stdin.readline
N, x = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(array, target, start, end, isleft):
    answer = -1
    while start <= end:
        mid = (start + end) // 2

        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            answer = mid
            if isleft:
                end = mid - 1
            else:
                start = mid + 1
    return answer 

def search(array, target, start, end):
    left_idx = binary_search(array, target, start, end, True)
    if left_idx == -1:
        return -1
    else:
        right_idx = binary_search(array, target, start, end, False)
        return right_idx - left_idx + 1

answer = search(arr, x, 0, N - 1)
print(answer)