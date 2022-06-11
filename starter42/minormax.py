t = int(input())

for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))

	if n <= 2:
		print("YES")
	else:
		minimum = min(arr[0], arr[1])
		maximum = max(arr[0],arr[1])

		possible = True
		for i in range(2, n):
			x = arr[i]

			if x >= maximum:
				maximum = x
			elif x <= minimum:
				minimum = x
			else:
				print("NO")
				possible = False
				break

		if possible:
			print("YES")