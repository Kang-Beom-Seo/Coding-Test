import sys

MAX = int(1e6)
input = sys.stdin.readline
isexist = [0 for _ in range(MAX + 1)]
N = int(input())
store = list(map(int, input().split()))
M = int(input())
customer = list(map(int, input().split()))

for element in store:
    isexist[element] = 1

for element in customer:
    if isexist[element] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')