import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ret = []

def dfs(i):
	if len(ret) == m:
		print(*ret)
		return
	for j in range(i, n + 1):
		if j >= i:
			ret.append(j)
			dfs(j)
			ret.pop()

dfs(1)