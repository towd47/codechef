import math
def nearestPow2(n):
	return 2 ** int(math.log(n, 2))

t = int(input())

for _ in range(t):
	n = int(input())
	data = list(map(int, input().split()))

	used = set()
	for x in data:
		while x > 0:
			pow2 = nearestPow2(x)
			used.add(pow2)
			x = x - pow2

	print(len(used))
