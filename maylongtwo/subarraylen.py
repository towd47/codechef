t = int(input())
for _ in range(t):
	n = int(input())
	data = list(map(int, input().split()))

	lastPos = {}

	count = 0

	for i in range(n):
		val = data[i]
		tot = val
		if val in lastPos and i - lastPos[val] < val:
			tot = i - lastPos[val]
		elif val > i:
			tot -= val - (i + 1)
		if val > n - i:
			tot -= val - (n - i)
		if tot < 0:
			tot = 0
		count += tot
		lastPos[val] = i

	print(count)
