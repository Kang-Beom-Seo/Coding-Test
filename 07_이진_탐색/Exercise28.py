import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return -1

answer = binary_search(arr, 0, N - 1)
print(answer)