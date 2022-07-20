'''
스택 2개를 다 비교하는 방법
'''

import sys

n = int(sys.stdin.readline())
wait = list(map(int, sys.stdin.readline().split()))
target = 1
tmp = []
while target != n:
	if wait and wait[0] == target:
		wait.pop(0)
		target += 1
	elif tmp and tmp[-1] == target:
		tmp.pop()
		target += 1
	else:
		tmp.append(wait.pop(0))
		if len(tmp) > 1 and tmp[-1] > tmp[-2]:
			print("Sad")
			sys.exit()
if (len(wait) == 1 and len(tmp) == 0 and target == wait[0]) or (len(wait) == 0 and len(tmp) == 1 and target == tmp[0]) :
	print("Nice")
else:
	print("Sad")


'''
스택 1개로 비교하는 방법
'''

import sys

input = sys.stdin.readline
n = int(input())
wait = list(map(int, input().split()))
tmp = []
target = 1
for i in wait:
	tmp.append(i)
	while tmp and tmp[-1] == target:
		tmp.pop()
		target += 1
	if len(tmp) > 1 and tmp[-1] > tmp[-2]:
		print("Sad")
		sys.exit()
if tmp:
	print("Sad")
else:
	print("Nice")
