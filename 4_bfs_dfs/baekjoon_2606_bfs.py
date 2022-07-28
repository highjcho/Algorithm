import sys

input = sys.stdin.readline
n = int(input())
t = int(input())
c = [[] for i in range(n + 1)]
q = []
visit = [0] * (n + 1)

for i in range(t):
	c1, c2 = map(int, input().split())
	c[c1].append(c2)
	c[c2].append(c1)

q.append(1)

while q:
	tmp = q.pop(0)
	visit[tmp] = 1
	for i in c[tmp]:
		if visit[i] != 1:
			visit[i] = 1
			q.append(i)

print(visit[2:].count(1))