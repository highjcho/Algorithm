import sys

n, k = map(int, sys.stdin.readline().split())
people = [i + 1 for i in range(n)]
ret = []
i = 0
while people:
	i = (i + k - 1) % len(people)
	ret.append(str(people.pop(i)))
print("<"+', '.join(ret)+">")