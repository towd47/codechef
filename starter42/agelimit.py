t = int(input())

for _ in range(t):
	x, y, a = list(map(int, input().split()))

	if a >= x and a < y:
		print("YES")
	else:
		print("NO")