import sys, heapq

input = sys.stdin.readline
n = int(input())
left = []
right = []
for i in range(n):
	num = int(input())
	if len(left) == len(right):
		heapq.heappush(left, -num)
	else:
		heapq.heappush(right, num)
	if right and -left[0] > right[0]:
		heapq.heappush(left, -heapq.heappop(right))
		heapq.heappush(right, -heapq.heappop(left))
	print(-left[0])