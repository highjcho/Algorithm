import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
cnt = 0

for _ in range(m):
	u, v = map(int, input().split())
	g[u].append(v)
	g[v].append(u)

def dfs(i):
	visit[i] = 1
	for j in g[i]:
		if visit[j] == 0:
			dfs(j)

for i in range(1, n + 1):
	if visit[i] == 0 and g[i]:
		dfs(i)
		cnt += 1
	if visit[i] == 0 and not g[i]:
		cnt += 1

print(cnt)