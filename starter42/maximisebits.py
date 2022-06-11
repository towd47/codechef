t = int(input())

for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.reverse()

	q = 0
	start = 0
	str1arr = []
	str2arr = []
	for i in range(n-1):
		if arr[i] <= arr[i+1]:
			diff = arr[i+1] - arr[i]
			str1 = str(n - (n - start) + 1) + " " + str(diff + 1)
			str2 = ""
			for j in range(n - i, n + 1):
				str2 = str2 + str(j) + " "
			str2.strip()
			start = i + 1
			q += 1
			str1arr.append(str1)
			str2arr.append(str2)

	print(q)
	for i in range(q):
		print(str1arr[i])
		print(str2arr[i])
