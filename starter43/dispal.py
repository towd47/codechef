alphabet = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())

for _ in range(t):
	n, x = list(map(int, input().split()))

	if x > int(n/2) + 1 or (n % 2 == 0 and x > int(n/2)):
		print(-1)
	else:
		if n <= 2:
			print('a' * n)
		else:
			string = alphabet[:min(x, 26)]
			reverse = string[::-1]
			if n % 2 == 1:
				reverse = reverse[1:]
			string += reverse
			middle = string[int(len(string)/2)]

			missing = n - len(string)
			middle = middle * missing
			string = string[:int(len(string)/2)] + middle + string[int(len(string)/2):]

			print(string)
		