import math
t = int(input())

for _ in range(t):
	n = int(input())
	if n == 1:
		print(1)
		print(1)
	elif n % 2 != 0:
		print(-1)
	else:
		matches = {}
		a = list(range(n, 0, -1))
		b = []

		for x in a:
			if x in matches:
				b.append(matches[x])
			else:
				val = x ^ (2**(int(math.log2(x)) + 1) - 1)
				if val == 0:
					val = 2**(int(math.log2(x)) + 1)
				b.append(val)
				matches[x] = val
				matches[val] = x

		print(" ".join([str(e) for e in a]))
		print(" ".join([str(e) for e in b]))