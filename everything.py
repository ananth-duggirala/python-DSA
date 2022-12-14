# The Stack abstract data type
# Stack(): initialize stack, push(item), pop(), peek(), isEmpty(), size()
class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

# The Queue abstract data type
# Queue(): initialize queue, enqueue(item), dequeue(), isEmpty(), size()

class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

# The Deque abstract data structure
# Deque(): initialize deque, addFront(item), addRear(item), removeFront(), removeRear(), isEmpty(), size()

class Deque:
	def __init__(self):
		self.items = []

	def addFront(self, item):
		self.items.insert(0, item)

	def addRear(self, item):
		self.items.append(item)

	def removeFront(self):
		return self.items.pop(0)

	def removeRear(self):
		return self.items.pop()

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

# The list abstract data type
# List(), add(item), remove(item), search(item), isEmpty(), size(), append(item), index(item), insert(pos, item), pop(), pop(pos)

# Linked list implementation
# Create a Node class: Node(), getData, getNext, setData, setNext
# Create an UnorderedList class: UnorderedList(), isEmpty(), add(item), size(), search(item), remove(item) 
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
	def getData(self):
		return self.data

	def setData(self, data):
		self.data = data

	def getNext(self):
		return self.next

	def setNext(self, nxt):
		self.next = nxt

class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		size = 0
		while current != None:
			size += 1
			current = current.next
		return size

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

# TODO: MazeRunner

# Dynamic programming: making change

def dpMakeChange(coinValueList, change, minCoins):
	for cents in range(change+1):
		coinCount = cents
		for j in [c for c in coinValueList if c <= cents]:
			if minCoins[cents-j] + 1 < coinCount:
				coinCount = minCoins[cents-j] + 1
		minCoins[cents] = coinCount
	return minCoins[change]


# Trees
# List of lists representation
myTree = ['a',['b', ['d',[],[]], ['e',[],[]]], ['c', ['f',[],[]], []] ]

def BinaryTree(r):
	return [r, [], []]

def insertLeft(root, newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch,[],[]])
	return root

def insertRight(root, newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2, [newBranch,[],t])
	else:
		root.insert(2,[newBranch,[],[]])
	return root

# Nodes and references representation
class BinaryTree:
	def __init__(self,rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t
	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

# Also define getLeftChild, getRightChild, setRootVal, getRootVal in the normal manner

# Preorder, inorder, and postorder
def preorder(tree):
	if tree:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

# Binary Heap
# BinaryHeap(), insert(k), findMin(), delMin(), isEmpty(), size(), buildHeap(list)

# heapq module: 
# heappush(heap, item), heappop(heap), heappushpop(heap,item), 
# heapify(x), heapreplace(heap,item), merge(*iterables, key=None, reverse=False)
# nlargest(n, iterable, key=None), nsmallest(n, iterable, key=None)


# TODO: Binary search tree in more detail

class BinarySearchTree:
	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

# Graphs:
# Adjacency matrix representation
class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for row in range(vertices)] for column in range(vertices)]

	def printGraph(self):
		for i in range(self.V):
			for j in range(self.V):
				print(self.graph[i][j], end=" ")
			print('\n')

	def addEdge(self,v,w):
		self.graph[v][w] = 1
		self.graph[w][v] = 1

class GraphAdjList:
	def __init__(self, vertices, edges):
		self.V = vertices
		self.adjList = [[] for i in range(vertices)]
		for (u,v) in edges:
			self.adjList[u].append(v)
