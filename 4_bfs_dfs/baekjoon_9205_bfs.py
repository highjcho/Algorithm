import sys

input = sys.stdin.readline
t = int(input())

def bfs():
	while q:
		cur_x, cur_y = q.pop(0)
		if abs(e_x - cur_x) + abs(e_y - cur_y) <= 1000:
			return "happy"
		for i in range(c):
			if visit[i] == 0:
				nx, ny = c_list[i][0], c_list[i][1]
				if abs(nx - cur_x) + abs(ny - cur_y) <= 1000:
					q.append((nx, ny))
					visit[i] = 1
	return "sad"

for _ in range(t):
	c = int(input())
	x, y = map(int, input().split())
	c_list = []
	for _ in range(c):
		c_x, c_y = map(int, input().split())
		c_list.append((c_x, c_y))
	e_x, e_y = map(int, input().split())
	visit = [0] * c
	q = []
	q.append((x, y))
	print(bfs())