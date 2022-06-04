t = int(input())

for _ in range(t):
	n, x, y = list(map(int, input().split()))
	data = list(map(int, input().split()))

	nocSum = 0
	cSum = x

	for e in data:
		nocSum += e
		cSum += max(0, e - y)

	if cSum < nocSum:
		print("COUPON")
	else:
		print("NO COUPON")
