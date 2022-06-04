t = int(input())

for _ in range(t):
	n = int(input())
	data = list(map(int, input().split()))

	x = 0
	n = n - 1
	while x == 0 and n >= 0:
		x = data[n]
		n -= 1
	print(n + 1)
