t = int(input())

for i in range(t):
	data = input()
	x, y = data.split()
	x = int(x)
	y = int(y)

	z = y - x
	if z <= 0:
		k = 0
	else:
		k = int(z / 8)
		if z % 8 != 0:
			k = k+1

	print(k)