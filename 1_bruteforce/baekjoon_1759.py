from itertools import combinations

l, c = map(int, input().split())
g = input().split()
g.sort()

com = list(combinations(range(c), l))
for i in com:
	w_c = l
	v_c = 1
	c_c = 2
	ret = []
	for j in i:
		if g[j] == 'a' or g[j] == 'e' or g[j] == 'i' or g[j] == 'o' or g[j] == 'u':
			if w_c <= c_c:
				break
			ret.append(g[j])
			w_c -= 1
			v_c -= 1
		else:
			ret.append(g[j])
			w_c -= 1
			c_c -= 1
	if not w_c and v_c != 1:
		print(''.join(ret))

from itertools import combinations

l, c = map(int, input().split())
g = input().split()
g.sort()
com = list(combinations(g, l))
v = ['a', 'e', 'i', 'o', 'w']

for pwd in com:
	v_c = 0
	for i in pwd:
		if i in v:
			v_c += 1
	if 1 <= v_c <= l - 2:
		print(''.join(pwd))
