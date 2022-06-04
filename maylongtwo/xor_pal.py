t = int(input())

for _ in range(t):
	n = int(input())
	b = input()

	count = 0
	for i in range(int(n/2)):
		if b[i] != b[n-1-i]:
			count += 1
	print(int(count / 2) + count % 2)