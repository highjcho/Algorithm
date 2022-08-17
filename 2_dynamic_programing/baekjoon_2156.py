import sys

input = sys.stdin.readline
n = int(input())
w = [int(input()) for _ in range(n)]
dp = [0] * n

dp[0] = w[0]
if n > 1:
	dp[1] = w[0] + w[1]
if n > 2:
	dp[2] = max(dp[1], max(w[0], w[1]) + w[2])
for i in range(3, n):
	dp[i] = max(dp[i - 1], w[i] + w[i - 1] + dp[i - 3], w[i] + dp[i - 2])
print(max(dp))