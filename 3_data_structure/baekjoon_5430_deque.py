import sys

input = sys.stdin.readline
t = int(input())

for i in range(t):
	cmd = input().rstrip()
	n = int(input())
	n_li = input().rstrip()[1:-1].split(',')
	rev = 0
	flag = 0
	for a in cmd:
		if a == 'R':
			rev += 1
		elif a == 'D':
			if not n_li or n == 0:
				print("error")
				flag = 1
				break
			else:
				if rev % 2 == 0:
					n_li.pop(0)
				else:
					n_li.pop()
	if not flag and rev % 2 == 0:
		print("[" + ",".join(n_li) + "]")
	elif not flag and rev % 2 != 0:
		n_li.reverse()
		print("[" + ",".join(n_li) + "]")
		

from collections import deque

t = int(input())

for i in range(t):
	p = input()
	n = int(input())
	arr = input()[1:-1].split(',')

	queue = deque(arr)

	flag = 0

	if n == 0:
		queue = []

	for j in p:
		if j == 'R':
			flag += 1
		elif j == 'D':
			if len(queue) == 0:
				print("error")
				break
			else:
				if flag % 2 == 0:
					queue.popleft()
				else:
					queue.pop()

	else: # error 후 여기에 안들어오는 이유가 뭐지? <- for - else 문!
		if flag % 2 == 0:
			print("[" + ",".join(queue) + "]")
		else:
			queue.reverse()
			print("[" + ",".join(queue) + "]")