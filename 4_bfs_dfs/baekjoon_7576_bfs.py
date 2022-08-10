from collections import deque
import sys

input = sys.stdin.readline
m, n = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
d = deque([])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
	for j in range(m):
		if g[i][j] == 1:
			d.append([i, j])

def bfs():
	while d:
		cx, cy = d.popleft()
		for x, y in zip(dx, dy):
			nx = cx + x
			ny = cy + y
			if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
				g[nx][ny] = g[cx][cy] + 1
				d.append([nx, ny])

bfs()

ret = 0
for i in g:
	if 0 in i:
		print(-1)
		break
	ret = max(ret, max(i))

else:
	print(ret - 1)