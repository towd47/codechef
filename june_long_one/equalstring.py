t = int(input())

for _ in range(t):
	n = int(input())
	a = input()
	b = input()

	newa = ""
	newb = ""

	for i in range(n):
		if a[i] != b[i]:
			newa += a[i]
			newb += b[i]

	bset = set()

	for x in newb:
		bset.add(x)

	print(len(bset))