import sys
from itertools import combinations as com

input = sys.stdin.readline
n, m = map(int, input().split())
h = []
c = []
for i in range(n):
	g = list(map(int, input().split()))
	for j in range(n):
		if g[j] == 1:
			h.append((i, j))
		if g[j] == 2:
			c.append((i, j))

c_l = list(com(c, m))
ret = 100000
for s_c in c_l:
	tmp_ret = 0
	for s_i in h:
		tmp = min([abs(c_i[0] - s_i[0]) + abs(c_i[1] - s_i[1]) for c_i in s_c])
		tmp_ret += tmp
	ret = min(ret, tmp_ret)
print(ret)