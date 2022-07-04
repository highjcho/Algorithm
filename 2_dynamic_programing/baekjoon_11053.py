import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = [1] * n
for i in range(n):
	for j in range(i):
		if num[j] < num[i] and dp[i] <= dp[j]:
			dp[i] = dp[j] + 1
print(max(dp))