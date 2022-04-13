n, k = map(int, input().split())
result = 0

while True:
    diff = n - ((n // k) * k)
    result += diff
    n = n // k
    result += 1
    if n == 0:
        break
result -= 2
print(result)