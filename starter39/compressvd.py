t = int(input())

for _ in range(t):
	n = int(input())
	data = list(map(int, input().split()))

	removeable = 0
	for x in range(n - 1):
		if data[x] == data[x+1]:
			removeable += 1

	print(n - removeable)