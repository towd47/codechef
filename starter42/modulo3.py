def findMinOps(arr):

	newarr = []
	for x in arr:
		a = x[0]
		b = x[1]
		if a % 3 == 0 or b % 3 == 0:
			return 0
		diff = int(abs(a - b))
		newarr.append((a, diff))
		newarr.append((diff, b))

	return findMinOps(newarr) + 1

t = int(input())

for _ in range(t):
	a, b = list(map(int, input().split()))

	arr = [(a, b)]
	print(findMinOps(arr))

