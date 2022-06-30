import sys

seven = [int(sys.stdin.readline()) for i in range(9)]
ret = sum(seven)
flag = 0
for i in range(8):
	for j in range(i + 1, 9):
		if (ret - (seven[i] + seven[j]) == 100):
			a, b = seven[i], seven[j]
			seven.remove(a)
			seven.remove(b)
			seven.sort()
			flag = 1
			for k in range(7):
				print(seven[k])
			break
	if (flag == 1):
		break