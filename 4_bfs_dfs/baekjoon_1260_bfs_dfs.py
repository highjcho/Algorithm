import sys

input = sys.stdin.readline
n, m, v = map(int, input().split())
g = [[] for i in range(n + 1)]
visit = [0] * (n + 1)
q = []

for i in range(m):
	g1, g2 = map(int, input().split())
	g[g1].append(g2)
	g[g2].append(g1)

def dfs(s):
	q.append(s)
	while q:
		tmp = q.pop()
		visit[tmp] = 1
		print(tmp, end=' ')
		g[tmp].sort()
		for i in g[tmp]:
			if visit[i] != 1:
				dfs(i)

def bfs(s):
	q.append(s)
	while q:
		tmp = q.pop(0)
		visit[tmp] = 1
		print(tmp, end=' ')
		for i in g[tmp]:
			if visit[i] != 1:
				visit[i] = 1
				q.append(i)

dfs(v)
print()
visit = [0] * (n + 1)
bfs(v)