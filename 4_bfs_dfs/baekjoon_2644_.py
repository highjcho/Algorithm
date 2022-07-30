'''
BFS
'''

import sys

input = sys.stdin.readline

n = int(input())
c1, c2 = map(int, input().split())
t = int(input())
visit = [0] * (n + 1)
 
g = [[] for _ in range(n + 1)]
for _ in range(t):
	p, c = map(int, input().split())
	g[p].append(c)
	g[c].append(p)

q = []
q.append((c1, 0))

def bfs():
	while q:
		w, r = q.pop(0)
		visit[w] = 1
		for i in g[w]:
			if i == c2:
				return (r + 1)
			if not visit[i]:
				q.append((i, r + 1))
	return (-1)

print(bfs())


'''
DFS
'''

import sys

input = sys.stdin.readline

n = int(input())
c1, c2 = map(int, input().split())
t = int(input())
d = [-1] * (n + 1)

g = [[] for _ in range(n + 1)]
for _ in range(t):
	p, c = map(int, input().split())
	g[p].append(c)
	g[c].append(p)

def dfs(g, w):
	for i in g[w]:
		if i == c2:
			d[i] = d[w] + 1
		if d[i] == -1:
			d[i] = d[w] + 1
			dfs(g, i)

d[c1] = 0
dfs(g, c1)
print(d[c2])