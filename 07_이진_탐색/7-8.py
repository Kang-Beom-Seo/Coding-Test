import sys

input = sys.stdin.readline
N, M = map(int, input().split())
rice_cakes = list(map(int, input().split()))

def get_total_length(array, H):
    answer = 0
    for cake in array:
        answer += max(0, cake - H)
    return answer

def binary_search(array, target, start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        total = get_total_length(array, mid)

        if total >= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer

answer = binary_search(rice_cakes, M, 0, max(rice_cakes))
print(answer)