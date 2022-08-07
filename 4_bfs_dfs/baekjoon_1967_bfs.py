import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
g = [[] for _ in range(n + 1)]
ret = 0
for _ in range(1, n):
	a, b, c = map(int,input().split())
	g[a].append((b, c))

def dfs(p, d):
	left, right = 0, 0
	for c, w in g[p]:
		tmp = dfs(c, w)
		if left <= right:
			left = max(left, tmp)
		else:
			right = max(right,tmp)
	global ret
	ret = max(ret, left + right)
	return max(left + d, right + d)

dfs(1 , 0)
print(ret)

'''
하드코딩..
'''

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
	p, c, w = map(int, input().split())
	g[p].append((c, w))
	g[c].append((p, w))

def bfs(i):
	visit = [0] * (n + 1)
	max = 0
	visit[i] = 1
	d = deque([i])
	while d:
		c = d.popleft()
		if i != c and len(g[c]) == 1:
			if max < visit[c]:
				max = visit[c]
			continue
		for p in g[c]:
			if not visit[p[0]]:
				visit[p[0]] = visit[c] + p[1]
				d.append(p[0])
	if max == 0:
		max = visit[c]
	return max - 1

ret = 0
max = 0
for i in range(1, n + 1):
	if len(g[i]) == 1:
		max = bfs(i)
	if ret < max:
		ret = max
print(ret)