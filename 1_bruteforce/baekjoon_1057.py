# import sys

# n, a, b = map(int, sys.stdin.readline().split())
# ret = 1
# if a > b:
# 	tmp = a
# 	a = b
# 	b = tmp

# while a // 2 + 1 != b // 2 or b - a > 1:
# 	if a % 2 == 0:
# 		a = a // 2
# 	else:
# 		a = a // 2 + 1
# 	if b % 2 == 0:
# 		b = b // 2
# 	else:
# 		b = b // 2 + 1
# 	ret += 1
# print(ret)

'''
깔끔 ver
'''
import sys

N, Kim, Im = map(int, sys.stdin.readline().split())
count = 0
while Kim != Im:
	Kim -= Kim // 2
	Im -= Im // 2
	count += 1
	print(f"kim: {Kim}, im: {Im}")
print(count)