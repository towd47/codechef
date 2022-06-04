t = int(input())

for _ in range(t):
	input()
	string = input()
	clgorr = 0
	for x in string:
		if x == 'c' or x == 'g' or x == 'l' or x == 'r':
			clgorr += 1
	print(2 ** clgorr % (10 ** 9 + 7))
