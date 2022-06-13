import math
t = int(input())

for _ in range(t):
	a, b = list(map(int, input().split()))
	x = a
	y = b
	ops = 0

	while x > 0 and y > 0:
		xlog = int(math.log2(x))
		ylog = int(math.log2(y))
		diff = abs(xlog - ylog)
		
		# This optimization cuts down ~ 3 seconds of run time off worst case
		if diff > 1:
			if x > y:
				y = y * (2 ** (diff - 1))
			else:
				x = x * (2 ** (diff - 1))
			ops += diff - 1
		elif x * 2 <= y:
			x = x * 2
			ops += 1
		elif y * 2 <= x:
			y = y * 2
			ops += 1
		elif x == y:
			ops += x
			x = 0
			y = 0
		else:
			diff = abs(x - y)
			val = min(x, y) - diff
			x -= val
			y -= val
			ops += val

	if x == 0 and y == 0:
		print(ops)
	else:
		print(-1)
