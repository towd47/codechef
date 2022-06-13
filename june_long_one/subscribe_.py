t = int(input())

for _ in range(t):
	n, x = list(map(int, input().split()))

	subs = int(n/6)
	if n%6 != 0:
		subs += 1

	print(subs * x)