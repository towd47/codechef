t = int(input())

for _ in range(t):
	n, k = list(map(int, input().split()))

	fives = int((n - 1) / 5) + 1

	kfive = int((k - 1) / 5) + 1

	print(fives - kfive)