import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ret = []

def dfs():
	if len(ret) == m:
		print(*ret)
		return

	for i in range(1, n + 1):
		if i not in ret:
			ret.append(i)
			dfs()
			ret.pop()

dfs()
