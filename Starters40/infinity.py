t = int(input())

for _ in range(t):
	n = int(input()) - 1

	steps = int(n/5) * 2

	n = n % 5
	if n > 3:
		steps += 1
	if n != 0:
		steps += 1

	print(steps)
