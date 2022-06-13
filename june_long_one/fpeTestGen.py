import random

cases = 1 # 2*10^4 max

f = open("fpeTest.txt", 'w')

string = str(cases) + "\n"

for _ in range(cases):
	n = 300000 # max 3*10^5
	string += str(n) + "\n"
	for i in range(n):
		string += str(random.randint(0, 1000000000))
		if i != n - 1:
			string += " "
	string += "\n"
	for i in range(n - 1):
		string += str(i + 1) + " " + str(i + 2) + "\n"

f.write(string)


