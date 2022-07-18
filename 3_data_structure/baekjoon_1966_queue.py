import sys, heapq

t = int(sys.stdin.readline())
for i in range(t):
	n, m = map(int, sys.stdin.readline().split())
	idx_list = list(enumerate((map(int, sys.stdin.readline().split()))))
	hq = []
	for j in range(n):
		heapq.heappush(hq, -idx_list[j][1])
	cnt = 0
	while cnt <= n:
		if idx_list[0][0] == m and idx_list[0][1] == -hq[0]:
			cnt += 1
			break
		elif idx_list[0][1] == -hq[0]:
			del idx_list[0]
			heapq.heappop(hq)
			cnt += 1
		else:
			idx_list.append(idx_list[0])
			del idx_list[0]
	print(cnt)