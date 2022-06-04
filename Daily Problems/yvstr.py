t = int(input())

for _ in range(t):
	n = int(input())
	s = input()


	if len(s) == 0:
		print(0)

	else:
		letters = {}
		patterns = {}
		lastChar = None
		lastCharLen = 0
		curChar = s[0]
		lastStart = 0
		for i in range(1, n + 1):
			if i == n or s[i] != curChar:
				if curChar in letters:
					letters[curChar] = max(i - lastStart, letters[curChar])
				else:
					letters[curChar] = i - lastStart

				if lastChar != None:
					pattern = (lastChar, curChar)
					if pattern in patterns:
						patterns[pattern].append((lastCharLen, i-lastStart))
					else:
						patterns[pattern] = [(lastCharLen, i-lastStart)]
				lastCharLen = i - lastStart
				lastChar = curChar
				lastStart = i
				if i != n:
					curChar = s[i]
		total = 0
		for x in letters:
			total += letters[x]

		for x in patterns:
				


		print(letters)
		print(patterns)



