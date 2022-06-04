t = int(input())

for _ in range(t):
	n = int(input())
	data = list(map(int, input().split()))

	last = 0
	done = False
	for x in data:
		if x < last:
			print("No")
			done = True
			break
		else:
			last = x
	if not done:
		print("Yes")