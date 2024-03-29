import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
g = []
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
ret = 0
ret_rg = 0

for i in range(n):
  g.append(list(input().strip()))

def dfs(cx, cy, c):
	visit[cx][cy] = 1
	for x, y in zip(dx, dy):
		nx = cx + x
		ny = cy + y
		if 0 <= nx < n and 0 <= ny < n:
			if visit[nx][ny] == 0 and g[nx][ny] == c:
				dfs(nx, ny, c)

visit = [[0] * n for _ in range(n)]
for i in range(n):
	for j in range(n):
		if visit[i][j] == 0:
			dfs(i, j, g[i][j])
			ret += 1

for i in range(n):
	for j in range(n):
		if g[i][j] == 'G':
			g[i][j] = 'R'

visit = [[0] * n for _ in range(n)]
for i in range(n):
	for j in range(n):
		if visit[i][j] == 0:
			dfs(i, j, g[i][j])
			ret_rg += 1

print(ret, ret_rg)