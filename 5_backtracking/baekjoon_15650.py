import sys


import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ret = []

def dfs(i):
	if len(ret) == m:
		print(*ret)
		return
	for j in range(i, n + 1):
		if j not in ret:
			ret.append(j)
			dfs(j)
			ret.pop()

# for i in range(1, n + 1):
# 	ret.append(i)
# 	dfs(i)
# 	ret.clear()
dfs(1)