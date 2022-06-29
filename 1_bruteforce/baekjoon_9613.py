import sys
t = int(sys.stdin.readline())

def get_gcd(a, b):
	while b : # while문을 활용한 유클리드 호제법 구현
		a, b = b, a % b
	return a

for i in range(t):
	case = list(map(int, sys.stdin.readline().split()))
	n = case[0]
	sum = 0
	for j in range(1, n):
		for k in range(j + 1, n + 1):
			sum += get_gcd(case[j], case[k])
	print(sum)


"""
재귀문을 활용한 유클리드 호제법 구현
"""
def get_gcd(a, b):
	if b == 0: # 재귀문을 활용한 유클리드 호제법 구현
		return a
	return get_gcd(b, a % b)

"""
math 모듈 내 gcd 함수를 활용한 유클리드 호제법 구현
"""
import math

for i in range(t):
	case = list(map(int, sys.stdin.readline().split()))
	n = case[0]
	sum = 0
	for j in range(1, n):
		for k in range(j + 1, n + 1):
			sum += math.gcd(case[j], case[k]) # math 모듈 내 gcd 함수 활용
	print(sum)
