'''
bfs
'''

import sys

input = sys.stdin.readline
t = int(input())
x = [1, -1, 1, -1, 2, -2, 2, -2]
y = [2, 2, -2, -2, 1, 1, -1, -1]

def bfs(c_x, c_y):
	q = []
	q.append((c_x, c_y))
	c[c_x][c_y] += 1
	while q:
		c_x, c_y = q.pop(0)
		if c_x == e_x and c_y == e_y:
			return c[c_x][c_y]
		for dx, dy in zip(x, y):
			nx = c_x + dx
			ny = c_y + dy
			if 0 <= nx < size and 0 <= ny < size and c[nx][ny] == -1:
				q.append((nx, ny))
				c[nx][ny] = c[c_x][c_y] + 1

for _ in range(t):
	size = int(input())
	c = [[-1] * size for _ in range(size)]
	s_x, s_y = map(int, input().split())
	e_x, e_y = map(int, input().split())
	print(bfs(s_x, s_y))

'''
dfs의 경우 지도 크기가 커지면 안된다
dfs는 모든 경우를 다 찾으며 최솟값을 비교하기 때문에 시간이 오래걸림
'''

import sys

input = sys.stdin.readline
t = int(input())
sys.setrecursionlimit(10**6)
x = [1, -1, 1, -1, 2, -2, 2, -2]
y = [2, 2, -2, -2, 1, 1, -1, -1]

def dfs(cur_x, cur_y):
	for dx, dy in zip(x, y):
		nx = cur_x + dx
		ny = cur_y + dy
		if nx == e_x and ny == e_y:
			if c[e_x][e_y] == -1 or c[e_x][e_y] > c[cur_x][cur_y] + 1:
				c[e_x][e_y] = c[cur_x][cur_y] + 1
				break
		if 0 <= nx < size and 0 <= ny < size and (c[nx][ny] == -1  or c[nx][ny] > c[cur_x][cur_y] + 1):
			c[nx][ny] = c[cur_x][cur_y] + 1
			dfs(nx, ny)

for _ in range(t):
	size = int(input())
	c = [[-1] * size for _ in range(size)]
	s_x, s_y = map(int, input().split())
	e_x, e_y = map(int, input().split())
	if s_x == e_x and s_y and e_y:
		print(0)
		continue
	c[s_x][s_y] = 0
	dfs(s_x, s_y)
	print(c[e_x][e_y])