import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
for i in range(2, n + 1):
	if i % 6 == 0:
		dp[i] = 1 + min(dp[i // 2], dp[i // 3], dp[i - 1])
	elif i % 2 == 0:
		dp[i] = 1 + min(dp[i // 2], dp[i - 1])
	elif i % 3 == 0:
		dp[i] = 1 + min(dp[i // 3], dp[i - 1])
	else:
		dp[i] = 1 + dp[i - 1]
print(dp[n])

"""
형식의 차이. 상기 코드가 조금 더 빠름
"""

import sys

x = int(sys.stdin.readline())
dp = [0] * (x + 1)
for i in range(2, x + 1):
	dp[i] = 1 + dp[i - 1]
	if i % 3 == 0:
		dp[i] = min(dp[i], dp[i // 3] + 1)
	if i % 2 == 0:
		dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[x])