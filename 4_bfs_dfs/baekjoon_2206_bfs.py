import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
s = []
x = [1, 0, -1, 0]
y = [0, -1, 0, 1]

def bfs():
	q = deque()
	q.append([0, 0, 1])
	visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
	visit[0][0][1] = 1
	while q:
		cx, cy, w = q.popleft()
		if cx == n - 1 and cy == m - 1:
			return visit[cx][cy][w]
		for dx, dy in zip(x, y):
			nx = cx + dx
			ny = cy + dy
			if 0 <= nx < n and 0 <= ny < m:
				if s[nx][ny] == 1 and w == 1:
					visit[nx][ny][0] = visit[cx][cy][1] + 1
					q.append([nx, ny, 0])
				elif s[nx][ny] == 0 and visit[nx][ny][w] == 0:
					visit[nx][ny][w] = visit[cx][cy][w] + 1
					q.append([nx, ny, w])
	return -1

for i in range(n):
	s.append(list(map(int, list(input().strip()))))
print(bfs())


'''
시간 초과가 무조건 나는 하드코딩 ver
'''

# import sys
# from collections import deque
# input = sys.stdin.readline
# path = []
# n, m = map(int, input().split())

# cnt = 1
# for i in range(n):
# 	path.append(list(map(int, list(input().strip()))))
# 	cnt += path[i].count(1)

# 	path.append(list(map(int, list(input().strip()))))


# if n == 1 and m == 1 and path[0][0] == 0:
# 	print(0)
# else:
# 	prev = (0, 0)
# 	ret = []
# 	x = [1, 0, -1, 0]
# 	y = [0, -1, 0, 1]

# 	def bfs(c_x, c_y):
# 		q = deque()
# 		q.append((c_x, c_y))
# 		visit[c_y][c_x] += 1
# 		while q:
# 			c_x, c_y = q.popleft()
# 			if c_x == m - 1 and c_y == n - 1:
# 				ret.append(visit[c_y][c_x] + 1)
# 				return
# 			for dx, dy in zip(x, y):
# 				nx = c_x + dx
# 				ny = c_y + dy
# 				if 0 <= nx < m and 0 <= ny < n and visit[ny][nx] == -1 and path[ny][nx] == 0:
# 					q.append((nx, ny))
# 					visit[ny][nx] = visit[c_y][c_x] + 1
# 		ret.append(-1)

# 	def change_path(prev, cnt):
# 		prev_y = prev[0]
# 		prev_x = prev[1]
# 		for i in range(prev_y, n):
# 			for j in range(prev_x, m):
# 				if path[i][j] == 1:
# 					path[i][j] = 0
# 					if cnt != 0:
# 						path[prev[0]][prev[1]] = 1
# 					return ((i, j))
# 			prev_x = 0

# 	prev = (0, 0)
# 	for i in range(cnt):
# 		visit = [[-1] * m for _ in range(n)]
# 		bfs(0, 0)
# 		prev = change_path(prev, i)

# 	if max(ret) != -1:
# 		min_ret = max(ret)
# 		for i in ret:
# 			if i < min_ret and i != -1:
# 				min_ret = i
# 		print(min_ret)
# 	else:
# 		print(-1)