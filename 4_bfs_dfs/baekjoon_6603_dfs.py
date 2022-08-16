import sys

input = sys.stdin.readline

def dfs(dep, i):
	if dep == 6:
		print(*ret)
		return
	
	for i in range(i, k):
		if dep + k - i < 6:
			return
		ret.append(s[i])
		dfs(dep + 1, i + 1)
		ret.pop()

while True:
	g = list(map(int, input().split()))
	k = g[0]
	s = g[1:]
	if k == 0:
		break
	ret = []
	dfs(0, 0)
	print()