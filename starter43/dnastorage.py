t = int(input())

for _ in range(t):
	n = int(input())
	string = input()

	dna = ""

	for i in range(0, n, 2):
		bit = string[i:i+2]
		if bit == '00':
			dna += 'A'
		elif bit == '01':
			dna += 'T'
		elif bit == '10':
			dna += 'C'
		elif bit == '11':
			dna += 'G'
	print(dna)