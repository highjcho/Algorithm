'''
처음부터 탐색하는 방법
'''

import sys

input = sys.stdin.readline
n = int(input())
g = [list(map(int, input().split())) for i in range(n)]

dp = [0] * (n + 1)
for i in range(n):
	for j in range(i + g[i][0], n + 1):
		print(j)
		if dp[j] < dp[i] + g[i][1]:
			dp[j] = dp[i] + g[i][1]
		print(dp)

print(dp[-1])

'''
마지막부터 탐색하는 방법
'''

import sys

input = sys.stdin.readline
n = int(input())
g = [list(map(int, input().split())) for i in range(n)]

dp = [0] * (n + 1)
for i in range(n-1, -1, -1):
	if i + g[i][0] <= n:
		dp[i] = max(dp[i + 1], g[i][1] + dp[i + g[i][0]])
	else:
		dp[i] = dp[i + 1]

print(dp[0])