import sys, heapq

n = int(sys.stdin.readline())
card = []
for i in range(n):
	heapq.heappush(card, int(sys.stdin.readline()))
ret = 0
while len(card) != 1:
	tmp1 = heapq.heappop(card)
	tmp2 = heapq.heappop(card)
	tmp = tmp1 + tmp2
	heapq.heappush(card, tmp)
	ret += tmp
print(ret)