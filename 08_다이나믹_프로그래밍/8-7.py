N = int(input())
MOD = 796796
memo = [0 for _ in range(1001)]
memo[1] = 1
memo[2] = 3
for i in range(3, N + 1):
    memo[i] = ((memo[i - 2] * 2) % MOD + memo[i - 1] % MOD) % MOD
print(memo[N])