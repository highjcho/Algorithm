'''
stack 구조 활용
'''

import sys

s = sys.stdin.readline().rstrip()
stack = []
ret = 0
for c in s:
	if c == '(':
		stack.append(c)
	else:
		if stack:
			stack.pop()
		else:
			ret += 1
print(ret + len(stack))

'''
replace 함수 활용
'''

s = input()
while '()' in s:
	s = s.replace('()', "")
print (len(s))