import sys

n, w, l = map(int, input().split())
q = list(map(int, input().split()))
 
b = [0] * w
time = 0
 
while b:
    time += 1
    b.pop(0)
    if q:
        if sum(b) + q[0] <= l:
            b.append(q.pop(0))
        else:
            b.append(0)
print(time)

'''
delay 활용에 대한 생각을 나중에 해보자..
'''

# n, w, l = map(int, sys.stdin.readline().split())
# q = list(map(int, sys.stdin.readline().split()))
# b = []
# delay = 0
# while q:
#   for i in range(w):
#       b.append(q.pop(0))
#       if not q or q[0] + sum(b) > l:
#           break
#   if q and len(b) != w:
#       delay += w - 1
#   b.clear()
# print(w + n + delay)
