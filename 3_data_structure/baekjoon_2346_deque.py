'''
deque rotate 활용
'''

import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))
for i in range(n):
	p = deq.popleft()
	print(p[0], end=' ')
	if p[1] > 0:
		deq.rotate(-(p[1] - 1))
	else:
		deq.rotate(-p[1])

'''
리스트 활용
'''

import sys

n = int(sys.stdin.readline())
data = list(enumerate((map(int, sys.stdin.readline().split())), start = 1))
idx = 0

while data:
	ret = data.pop(idx)
	print(ret[0], end=' ')
	if ret[1] < 0 and data:
		idx = (idx + ret[1]) % len(data)
	elif ret[1] > 0 and data:
		idx = (idx + (ret[1] - 1)) % len(data)

'''
딕셔너리 자료형 사용의 잘못된 예 ㅠ
'''

# import sys

# n = int(sys.stdin.readline())
# d = list(map(int, sys.stdin.readline().split()))
# d_t = {0:0}
# for i in range(n):
# 	d_t[i] = i + 1
# ret = []
# next_idx = d[0]
# for i in range(n):
# 	cur_idx = d.index(next_idx)
# 	value = d[cur_idx]
# 	ret.append(d_t.get(value))
# 	if value > 0:
# 		next_idx = d[(cur_idx + value) % len(d)]
# 	else:
# 		if cur_idx + value >= 0:
# 			next_idx = d[cur_idx + value]
# 		else:
# 			next_idx = d[len(d) + value + cur_idx]
# 	del d[cur_idx]
# for r in ret:
# 	print(r, end=' ')