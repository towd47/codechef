data = list(map(int, input().split()))
complete = 0
for x in data:
	if x >= 10:
		complete += 1
print(complete)