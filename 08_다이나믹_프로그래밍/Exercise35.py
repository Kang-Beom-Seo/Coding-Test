from collections import defaultdict
from queue import PriorityQueue

n = int(input())
memo = defaultdict(bool)
memo[1] = True
ugly_numbers = PriorityQueue()
ugly_numbers.put(1)
cnt = 0
while cnt < n:
    now_number = ugly_numbers.get()
    cnt += 1
    for i in (2, 3, 5):
        if not memo[now_number * i]:
            ugly_numbers.put(now_number * i)
            memo[now_number * i] = True
print(now_number)