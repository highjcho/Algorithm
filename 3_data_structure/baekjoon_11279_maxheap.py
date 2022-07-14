import sys, heapq

max_heap = []
n = int(sys.stdin.readline())
for i in range(n):
	num = int(sys.stdin.readline()) * -1
	if num == 0:
		print(heapq.heappop(max_heap) * -1 if max_heap else 0)
	else:
		heapq.heappush(max_heap, num)