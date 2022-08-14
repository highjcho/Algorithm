import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
p = [i for i in range(n)]

ret = 10000
t = list(combinations(p, n//2))
c = len(t)
k = 0
for t1 in t:
	if k == c / 2:
		break
	s = 0
	l = 0
	t2 = list(set(p) - set(t1))
	for i in list(combinations(t1, 2)):
		s += g[i[0]][i[1]]
		s += g[i[1]][i[0]]
	for i in list(combinations(t2, 2)):
		l += g[i[0]][i[1]]
		l += g[i[1]][i[0]]
	tmp = abs(s - l)
	if tmp < ret:
		ret = tmp
	k += 1
print(ret)