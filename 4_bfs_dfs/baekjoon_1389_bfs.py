import sys

input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
	a, b = map(int, input().split())
	g[a].append(b)
	g[b].append(a)

def bfs(i):
	visit = [-1] * (n + 1)
	visit[i] = 0
	q = []
	q.append(i)
	while q:
		j = q.pop(0)
		for k in g[j]:
			if visit[k] == -1:
				visit[k] = visit[j] + 1
				q.append(k)
	return sum(visit[1:n + 1])

min_c = n * m
ret = 0
for i in range(1, n + 1):
	tmp = bfs(i)
	if min_c > tmp:
		ret = i
		min_c = tmp
print(ret)