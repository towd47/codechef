t = int(input())

for _ in range(t):
	n = int(input())
	s = input()

	count = 0
	last = None
	if s[0] == '1':
		count += 1

	for x in s:
		if last and last == '0' and x == '1':
				count += 1
		last = x

	if last == '0':
		count += 1

	print(count)

