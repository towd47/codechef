from math import gcd
from functools import reduce

def findgcd(vals):
	return reduce(gcd, vals)

class Node:
	def __init__(self, val, num):
		self.val = val
		self.num = num
		self.children = []
		self.visited = 0
		self.parent = None
		self.gcd = None
		self.beauty = 0

	def addLink(self, node):
		self.children.append(node)

	def __str__(self):
		string = str(self.num)
		string += " -> "
		for x in self.children:
			string += str(x.num) + " "
		return string

	def printTreeAsRoot(self):
		nodesToCheck = [self]
		while nodesToCheck:
			x = nodesToCheck.pop(0)
			print(x)
			nodesToCheck.extend(x.children)

	# RECURSIVE, CAN HIT RECURSIVE LIMIT IF TREE IS LARGE ENOUGH
	def printTreegcds(self):
		print(str(self.num) + ": " + str(self.gcd))
		for x in self.children:
			x.printTreegcds()

	# RECURSIVE, CAN HIT RECURSIVE LIMIT IF TREE IS LARGE ENOUGH
	def printTreeBeauties(self):
		print(str(self.num) + ": " + str(self.beauty))
		for x in self.children:
			x.printTreeBeauties()

	# RECURSIVE, CAN HIT RECURSIVE LIMIT IF TREE IS LARGE ENOUGH
	def calcgcd(self):
		vals = [self.val]
		for x in self.children:
			if x.gcd == None:
				x.calcgcd()
			vals.append(x.gcd)
		self.gcd = findgcd(vals)

	# RECURSIVE, CAN HIT RECURSIVE LIMIT IF TREE IS LARGE ENOUGH
	def calculateBeauty(self):
		if self.parent != None:
			self.beauty = self.parent.beauty - self.gcd
		for x in self.children:
			self.beauty += x.gcd
		for x in self.children:
			x.calculateBeauty()

	# RECURSIVE, CAN HIT RECURSIVE LIMIT IF TREE IS LARGE ENOUGH
	def maxBeauty(self):
		beautyMax = self.beauty
		for x in self.children:
			beautyMax = max(beautyMax, x.maxBeauty())
		return beautyMax

# NON RECURSIVE SOLUTION TO AVOID RECURSION DEPTH LIMITS
def findMaxBeauty(root):
	nodesToCheck = [root]
	maxBeauty = 0

	while nodesToCheck:
		node = nodesToCheck.pop()
		maxBeauty = max(node.beauty, maxBeauty)
		nodesToCheck.extend(node.children)

	return maxBeauty

# NON RECURSIVE SOLUTION TO AVOID RECURSION DEPTH LIMITS
def calcBeauties(root):
	nodesToCheck = [root]

	while nodesToCheck:
		node = nodesToCheck.pop()
		if node.parent != None:
			node.beauty += node.parent.beauty
			node.beauty -= node.gcd
		for x in node.children:
			node.beauty += x.gcd
			nodesToCheck.append(x)

# NON RECURSIVE SOLUTION TO AVOID RECURSION DEPTH LIMITS
def calcgcds(root):
	nodesToCheck = [root]

	while nodesToCheck:
		node = nodesToCheck.pop()
		notDone = []
		vals = [node.val]
		for x in node.children:
			if x.gcd == None:
				notDone.append(x)
			else:
				vals.append(x.gcd)
		if notDone:
			nodesToCheck.append(node)
			nodesToCheck.extend(notDone)
		else:
			node.gcd = findgcd(vals)

t = int(input())

for _ in range(t):
	nodes = {}
	n = int(input())
	vals = list(map(int, input().split()))

	for i in range(n):
		node = Node(vals[i], i+1)
		nodes[i+1] = node

	for _ in range(n - 1):
		l1, l2 = list(map(int, input().split()))

		nodes[l1].addLink(nodes[l2])
		nodes[l2].addLink(nodes[l1])

	root = nodes[1]
	nodesToCheck = [root]

	# Finds the parent nodes and assigns them as such
	# Then removes parent from children list
	while nodesToCheck:
		node = nodesToCheck.pop()
		for x in node.children:
			x.parent = node
			x.children.remove(node)
		nodesToCheck.extend(node.children)

	calcgcds(root)
	calcBeauties(root)
	print(findMaxBeauty(root))
