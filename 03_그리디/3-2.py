n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

num = m // (k + 1)
result = num * (first * k + second)
if m % (k + 1) != 0:
    result += first * (m % (k + 1))

print(result)