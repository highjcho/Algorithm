import sys, math


t = int(sys.stdin.readline())

'''
DP를 활용한 구현
'''

dp = [[0] * 30 for i in range(30)]
for i in range(30):
	for j in range(30):
		if i == 1:
			dp[i][j] = j
		elif i == j:
			dp[i][j] = 1
		elif i < j:
			dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
for i in range(t):
	n, m = map(int, sys.stdin.readline().split())
	print(dp[n][m])

'''
조합 계산 공식을 활용한 구현
'''

for i in range(t):
	n, m = map(int, sys.stdin.readline().split())
	ret = 1
	k = m - n
	while m > k:
		ret *= m
		m -= 1
	while n > 1:
		ret = ret // n
		n -= 1
	print(ret)

	# if mCn -> m! / (m - n)!n!
	# m * (m - 1) * ... * ((m - n) * (m - n - 1) * ... * 1)
	# ((m - n) * (m - n - 1) * ... * 1) * n * (n - 1) * ... * 1
	# 분모의 (m - n)!과 분자의 (m - n)! 부분은 동일하여 나눠서 사라짐
	# 분모는 m * (m - 1) * ... * (m - n + 1) 부분만 남음
	# 분자는 n * (n - 1) * ... * 1 부분만 남음
	# 따라서, m 부터 m - n 전 까지의 팩토리얼을 n!로 나눈 값이 결과가 됨

'''
조합 함수를 활용한 구현
'''

for i in range(t):
	n, m = map(int, sys.stdin.readline().split())
	print(math.comb(m, n))