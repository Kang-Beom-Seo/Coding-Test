N = int(input())
result = 0
for hour in range(N + 1):
    hour = str(hour)
    for minute in range(60):
        minute = str(minute)
        for second in range(60):
            second = str(second)
            if '3' in hour or '3' in minute or '3' in second:
                result += 1

print(result)