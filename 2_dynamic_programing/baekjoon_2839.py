import sys

n = int(sys.stdin.readline())
dp = [-1] * (n + 1)
dp[3] = 1
for i in range(5, n + 1):
	if i % 5 == 0:
		dp[i] = i // 5
	elif dp[i - 3] != -1:
		dp[i] = dp[i - 3] + 1
print(dp[n])