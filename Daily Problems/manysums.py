t = int(input())

for _ in range(t):
	l, r = list(map(int, input().split()))
	low = l + l
	high = r + r

	print(high - low + 1)