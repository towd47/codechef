t = int(input())

for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))

	val = sum(arr)

	if n % 2 != 0:
		print(-1)
	else:
		print(int(abs(val / 2)))