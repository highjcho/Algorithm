import sys

input = sys.stdin.readline

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def dfs(cx, cy):
	g[cx][cy] = 0
	for x, y in zip(dx, dy):
		nx = cx + x
		ny = cy + y
		if 0 <= nx < h and 0 <= ny < w and g[nx][ny]:
			dfs(nx, ny)

while True:
	w, h = map(int, input(). split())
	if w == 0 and h == 0:
		break
	cnt = 0
	g = [list(map(int, input().split())) for _ in range(h)]
	for i in range(h):
		for j in range(w):
			if g[i][j]:
				dfs(i, j)
				cnt += 1
	print(cnt)