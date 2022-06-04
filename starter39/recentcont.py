t = int(input())

for i in range(t):
	input()
	codes = input()
	codes = codes.split()
	s = 0
	l = 0
	for x in codes:
		if x == 'START38':
			s += 1
		else:
			l += 1

	print(str(s) + " " + str(l))