def doSwaps(b1, b2, l):
	swaps = []

	while b2 > b1:
		if l[b1] > l[b2]:
			i = biSearch(l[:b1 + 1], l[b2])
			l[i], l[b2] = l[b2], l[i]
			swaps.append((i, b2))
		else:
			b2 -= 1
	return [l, swaps]

def biSearch(arr, val):
	r = len(arr)
	l = 0
	i = int(r/2)
	found = False
	while not found:
		if i == 0:
			found = True
		elif arr[i] > val and arr[i-1] < val:
			found = True
		elif arr[i] > val:
			r = i
			i = int(i - (i - l)/2)
		else:
			l = i
			i = int((r - i)/2 + i)
	return i

t = int(input())

for _ in range(t):
	n = int(input())
	p = list(map(int, input().split()))

	arr1bounds = None
	arr2bounds = None

	i = 0
	bound1 = 0
	bound1Set = False
	swaps = []
	while i < n:
		if i == n - 1:
			if bound1Set:
				p, s = doSwaps(bound1, i, p)
				swaps.extend(s)
		elif p[i] > p[i+1]:
			if bound1Set:
				p, s = doSwaps(bound1, i, p)
				swaps.extend(s)
				bound1Set = False
				i -= 1
			else:
				bound1 = i
				bound1Set = True
		i += 1

	print(len(swaps))
	for x in swaps:
		print(str(x[0] + 1) + " " + str(x[1] + 1))
