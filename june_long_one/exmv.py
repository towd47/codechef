t = int(input())

for _ in range(t):
	x, n = list(map(int, input().split()))

	print((x-1) * (2 * n - x)