import math

def addToOddOneOut(l, val):
	if l[0] == l[1] and l[1] < l[2]:
		return None
	if l[0] == l[2] and l[2] < l[1]:
		return None
	if l[2] == l[1] and l[1] < l[0]:
		return None
	oddOne = None
	b0 = bin(l[0])[2:]
	b1 = bin(l[1])[2:]
	b2 = bin(l[2])[2:]
	b0 = '0' * 30 + b0
	b1 = '0' * 30 + b1
	b2 = '0' * 30 + b2

	pos = -1 * (val + 1)

	if b0[pos] == b1[pos] and b0[pos] != b2[pos]:
		oddOne = 2
	elif b0[pos] != b1[pos] and b0[pos] == b2[pos]:
		oddOne = 1
	elif b0[pos] != b1[pos] and b0[pos] != b2[pos]:
		oddOne = 0

	if oddOne != None:
		l[oddOne] += 2**val
		return l
	else:
		return None


t = int(input())

for _ in range(t):
	l = list(map(int, input().split()))
	val = 0
	equal = False
	while l and not equal:
		equal = l[0] == l[1] and l[1] == l[2]
		l = addToOddOneOut(l, val)
		val += 1
	if equal:
		print("YES")
	else:
		print("NO")






