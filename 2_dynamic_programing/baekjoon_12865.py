'''
2차원 dp 배열 구현
'''

import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[0] * (k + 1) for i in range(n + 1)]

for i in range(n):
	w, v = map(int, sys.stdin.readline().split())
	for j in range(1, k + 1):
		if j >= w:
			if dp[i][j - w] + v > dp[i][j]:
				dp[i + 1][j] = dp[i][j - w] + v
			else:
				dp[i + 1][j] = dp[i][j]
		else:
			dp[i + 1][j] = dp[i][j]
print(dp[n][k])

'''
1차원 dp 배열 구현
'''

import sys

n, k = map(int, sys.stdin.readline().split())
ret = [0] * (k + 1)
for i in range(n):
	w, v = map(int, sys.stdin.readline().split())
	if w > k:
		continue
	for j in range(k, 0, -1):
		if w + j <= k and ret[j] != 0:
			ret[w + j] = max(ret[w + j], ret[j] + v)
	ret[w] = max(ret[w], v)
print(ret[k])

'''
딕셔너리 자료형 구현
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
k += 1
items = [tuple(map(int, input().split())) for _ in range(n)]
items.sort(reverse=True)
dp = {0 : 0}

for w, v in items:
	tmp = {}
	for dp_v, dp_w in dp.items():
		if dp.get(nv:= dp_v + v, k) > (nw := dp_w + w):
			tmp[nv] = nw
	dp.update(tmp)
print(max(dp.keys()))