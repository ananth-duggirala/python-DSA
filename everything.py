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
# Create a Node class: getData, getNext, setData, setNext
# Create an UnorderedList class: 