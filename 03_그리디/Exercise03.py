S = input()

if len(S) == 1:
    print(0)
else:
    count = 0
    for i in range(1, len(S)):
        if S[i] != S[i - 1]:
            count += 1
    result = int((count + 1) / 2)
    print(result)