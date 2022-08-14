import sys

input = sys.stdin.readline
n = int(input())
g = [list(map(int, input().split())) for i in range(n)]

for i in range(1, n):
	g[i][0] += g[i - 1][0]
	g[i][i] += g[i - 1][i - 1]
	for j in range(1, i):
		g[i][j] += max(g[i - 1][j], g[i - 1][j - 1])
print(max(g[-1]))