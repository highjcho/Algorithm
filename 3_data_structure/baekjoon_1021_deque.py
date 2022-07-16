import sys

n, m = map(int, sys.stdin.readline().split())
idx = list(map(int, sys.stdin.readline().split()))
d = [i for i in range(1, n + 1)]
ret = 0
for i in range(m):
	for j in range(len(d)): # j = d.index(idx[i])
		if idx[i] == d[j]:
			break
	if j <= len(d) / 2:
		while idx[i] != d[0]:
			d.append(d.pop(0))
			ret += 1
	else:
		while idx[i] != d[0]:
			d.insert(0, d.pop())
			ret += 1
	d.pop(0)
print(ret)