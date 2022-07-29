import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
t = int(input())
global cnt

def dfs(cab, i, j):
	global cnt
	cab[i][j] = 0
	cnt += 1
	if i > 0 and cab[i - 1][j]:
		dfs(cab, i - 1, j)
	if i + 1 < n and cab[i + 1][j]:
		dfs(cab, i + 1, j)
	if j > 0 and cab[i][j - 1]:
		dfs(cab, i, j - 1)
	if j + 1 < m and cab[i][j + 1]:
		dfs(cab, i, j + 1)

for _ in range(t):
	m, n, k = map(int, input().split())
	cab = [[0] * m for i in range(n)]
	for _ in range(k):
		x, y = map(int, input().split())
		cab[y][x] = 1
	ret = 0
	cnt = 0
	for i in range(n):
		for j in range(m):
			if cab[i][j] == 1:
				dfs(cab, i, j)
				ret += 1
			if cnt == k:
				break
	print(ret)
