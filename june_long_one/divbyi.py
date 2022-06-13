t = int(input())

for _ in range(t):
	n = int(input())

	arr1 = list(range(1, int(n/2) + 1))
	arr1.reverse()

	arr2 = list(range(int(n/2) + 1, n+1))

	finalarr = []

	if len(arr2) > len(arr1):
		finalarr.append(arr2[0])
		arr2.pop(0)

	for i in range(len(arr1)):
		finalarr.append(arr1[i])
		finalarr.append(arr2[i])

	print(" ".join(str(x) for x in finalarr))

