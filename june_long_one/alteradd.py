t = int(input())

for _ in range(t):
	a, b = list(map(int, input().split()))

	diff = b - a

	if (diff - 1) % 3 == 0 or diff % 3 == 0:
		print("YES")
	else:
		print("NO")