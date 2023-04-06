from itertools import permutations
perm = permutations(input())
k = list(perm)
s = []
for i in k:
	d=''
	for j in i :
		d+=j
	s.append(d)
for i in s:
	if i == "silent":
		print(i)
		break