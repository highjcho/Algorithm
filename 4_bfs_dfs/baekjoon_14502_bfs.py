import sys
import copy

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
g = []
for i in range(n):
	g.append(list(map(int, input().split())))

ret = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
	global ret
	tmp_g = copy.deepcopy(g)
	q = []
	for i in range(n):
		for j in range(m):
			if tmp_g[i][j] == 2:
				q.append((i, j))
	while q:
		global cur_min
		cx, cy = q.pop(0)
		for x, y in zip(dx, dy):
			nx = cx + x
			ny = cy + y
			if 0 <= nx < n and 0 <= ny < m and tmp_g[nx][ny] == 0:
				q.append((nx, ny))
				tmp_g[nx][ny] = 2
	tmp = 0
	for i in range(n):
		tmp += tmp_g[i].count(0)
	ret = max(ret, tmp)

def dfs(cnt, x, y):
	if cnt == 3:
		bfs()
		return
	for i in range(x, n):
		for j in range(y, m):
			if g[i][j] == 0:
				g[i][j] = 1
				dfs(cnt + 1, i, j)
				g[i][j] = 0
		y = 0

dfs(0, 0, 0)
print(ret)