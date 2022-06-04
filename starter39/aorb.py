t = int(input())

for _ in range(t):
	data = input()
	x, y = data.split()
	x = int(x)
	y = int(y)

	a = (500 - x*2) + (1000 - (x + y) * 4)
	b = (1000 - y*4) + (500 - (x + y) * 2)

	print(max(a, b))