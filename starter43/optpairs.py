import math
def g(a, b):
	return math.gcd(a, b) + math.lcm(a, b)

t = int(input())

for _ in range(t):
	n = int(input())
	if n == 2:
		print(1)
	else:
		factors = set()

		for i in range(2, int(math.sqrt(n)) + 1):
			if n % i == 0:
				factors.add((i, n-i))
				factors.add((n-i, i))
				factors.add((int(n/i), n - int(n/i)))
				factors.add((n - int(n/i), int(n/i)))
		
		print(len(factors) + 2)

