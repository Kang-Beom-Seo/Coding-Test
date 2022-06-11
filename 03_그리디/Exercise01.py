N = int(input())
cnt = [0 for _ in range(N + 2)]
fears = list(map(int, input().split()))
for fear in fears:
    cnt[fear] += 1

group = 0
for i in range(1, N + 1):
    group += cnt[i] // i
    cnt[i + 1] += cnt[i] % i

print(group)