'''
priority queue 활용
'''

from queue import PriorityQueue
import sys

pq = PriorityQueue()
n = int(sys.stdin.readline())
for i in range(n):
	num = int(sys.stdin.readline())
	if num == 0:
		if pq.qsize() == 0:
			print(0)
		else:
			print(pq.get())
	else:
		pq.put(num)

'''
heapq 활용
'''

import heapq, sys

heap = []
n = int(sys.stdin.readline())
for i in range(n):
	num = int(sys.stdin.readline())
	if num == 0:
		if len(heap) == 0:
			print(0)
		else:
			print(heapq.heappop(heap))
	else:
		heapq.heappush(heap, num)