t = int(input())

for _ in range(t):
	n = int(input())
	l1 = list(map(int, input().split()))
	l2 = list(map(int, input().split()))

	pairs = {}

	for i in range(n):
		val = l1[i] ^ l2[i]
		if val in pairs:
			pairs[val] += 1
		else:
			pairs[val] = 1

	res = 0
	for pair in pairs:
		val = pairs[pair]
		res += val * (val - 1) / 2

	print(int(res))
