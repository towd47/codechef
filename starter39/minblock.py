class Node:
	def __init__(self, city):
		self.city = city
		self.children = []

	def addChild(self, child, roadval):
		self.children.append((child, roadval))

	def __str__(self):
		val = str(self.city) + ": "
		for x in self.children:
			val = val + str(x[0].city)
		return val

def getNumChildren(node):
	total = len(node.children)
	for child in node.children:
		total += getNumChildren(child[0])
	return total

def printChildren(node):
	print(str(node.city) + ':')
	for child in node.children:
		print(child[0].city)
	for child in node.children:
		printChildren(child[0])


t = int(input())

for _ in range(t):
	nodes = {}
	city1 = Node(1)
	nodes[1] = city1

	n, k = input().split()
	n = int(n)
	k = int(k)

	delayedq = []
	for _ in range(n - 1):
		u, v, x = input().split()
		u = int(u)
		v = int(v)
		x = int(x)

		
		delayedq.append((u, v, x))

	while delayedq:
		nextRoad = delayedq.pop(0)
		u = nextRoad[0]
		v = nextRoad[1]
		x = nextRoad[2]
		if not u in nodes and not v in nodes:
			delayedq.append(nextRoad)
		else:
			if u in nodes:
				cityu = nodes[u]
				cityv = Node(v)
				nodes[v] = cityv
				cityu.addChild(cityv, x)
			else:
				cityv = nodes[v]
				cityu = Node(u)
				nodes[u] = cityu
				cityv.addChild(cityu, x)

	nodesToCheck = [city1]
	blockedCitiesToCheck = []
	blockedByOneRoad = []
	while nodesToCheck:
		city = nodesToCheck.pop()
		for child in city.children:
			if child[1] == 1:
				blockedCitiesToCheck.append(child[0])
			else:
				nodesToCheck.append(child[0])

	while blockedCitiesToCheck:
		city = blockedCitiesToCheck.pop()
		blockedByOneRoad.append(getNumChildren(city) + 1)

	blockedByOneRoad.sort()
	totalBlocked = 0
	roadsBlocked = 0

	while blockedByOneRoad and (n - totalBlocked) > k:
		totalBlocked += blockedByOneRoad.pop()
		roadsBlocked += 1

	if n - totalBlocked <= k:
		print(roadsBlocked)
	else:
		print(-1)
