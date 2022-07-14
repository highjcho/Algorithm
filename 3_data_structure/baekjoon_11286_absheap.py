# import sys, heapq

# abs_heap = []
# n = int(sys.stdin.readline())
# for i in range(n):
# 	num = int(sys.stdin.readline())
# 	if num:
# 		heapq.heappush(abs_heap, (abs(num), num))
# 	else:
# 		if abs_heap:
# 			print(heapq.heappop(abs_heap)[1])
# 		else:
# 			print(0)

import sys, heapq

min_heap = []
max_heap = []
n = int(sys.stdin.readline())
for i in range(n):
	num = int(sys.stdin.readline())
	if num > 0:
		heapq.heappush(min_heap, num)
	elif num < 0:
		heapq.heappush(max_heap, -num)
	else:
		if min_heap:
			if max_heap:
				if min_heap[0] < max_heap[0]:
					print(heapq.heappop(min_heap))
				else:
					print(-heapq.heappop(max_heap))
			else:
				print(heapq.heappop(min_heap))
		elif max_heap:
			print(-heapq.heappop(max_heap))
		else:
			print(0)