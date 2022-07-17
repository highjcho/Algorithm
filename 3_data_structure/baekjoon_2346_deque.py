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
data = list(map(int, sys.stdin.readline().split()))
index = [x for x in range(1, n + 1)]
idx = 0
ret = []
temp = data.pop(idx)
ret.append(index.pop(idx))

while data:
	if temp < 0:
		idx = (idx + temp) % len(data)
	else:
		idx = (idx + (temp - 1)) % len(data)
	temp = data.pop(idx)
	ret.append(index.pop(idx))

for r in ret:
	print(r, end=' ')

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