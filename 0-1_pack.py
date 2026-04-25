import sys
N,W = map(int,sys.stdin.readline().split())
values = [0] * (N + 1)
weights = [0] * (N + 1)
i = 1
for line in sys.stdin.readlines():
    values[i], weights[i] = map(int, line.split())
    i += 1

dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, W + 1):
        if j < weights[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], values[i] + dp[i - 1][j - weights[i]])
print(dp[-1][-1])
