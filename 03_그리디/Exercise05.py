N, M = map(int, input().split())
K = list(map(int, input().split()))
answer = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if K[i] != K[j]:
            answer += 1

print(answer)