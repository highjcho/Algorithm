import sys

a, b = map(str, sys.stdin.readline().strip().split())
ret = []
for i in range(len(b) - len(a) + 1):
	cnt = 0
	for j in range(len(a)):
		if a[j] != b[i + j]:
			cnt += 1
	ret.append(cnt)
print(min(ret))