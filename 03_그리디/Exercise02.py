S = list(map(int, input()))
N = len(S)
answer = S[0]
for i in range(1, N):
    answer = max(answer + S[i], answer * S[i])
print(answer)