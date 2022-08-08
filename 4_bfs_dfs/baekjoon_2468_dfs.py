import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
g = []
max_h = 0
for i in range(n):
	g.append(list(map(int, input().split())))
	max_h = max(max(g[i]), max_h)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(i, cx, cy):
	visit[cx][cy] = 1
	for x, y in zip(dx, dy):
		nx = cx + x
		ny = cy + y
		if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and g[nx][ny] > i:
			dfs(i, nx, ny)

ret = 0
for i in range(0, max_h):
	visit = [[0] * n for _ in range(n)]
	cnt = 0
	for j in range(n):
		for k in range(n):
			if g[j][k] > i and visit[j][k] == 0:
				dfs(i, j, k)
				cnt += 1
	if cnt > ret:
		ret = cnt

print(ret)