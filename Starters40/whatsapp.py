t = int(input())

for _ in range(t):
	data = list(map(int, input().split()))

	result = (data[0] - data[1]) * data[2]
	print(result)