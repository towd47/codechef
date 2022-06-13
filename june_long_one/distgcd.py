from functools import reduce

t = int(input())

for _ in range(t):
	a, b = list(map(int, input().split()))
	n = abs(a - b)

	divisors = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

	print(len(divisors))