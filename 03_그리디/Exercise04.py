N = int(input())
cnt = [0 for _ in range(1000001)]
coins = list(map(int, input().split()))
for coin in coins:
    cnt[coin] += 1
for i in range(1, 1000000001):
    now = i
    money = i
    while money > 0 and now > 0:
        max_cnt = (money // now)
        money -= min(max_cnt, cnt[now]) * now
        now = min(now - 1, money)
    if money > 0:
        print(i)
        break