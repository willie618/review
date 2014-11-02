#!/usr/bin/python
import Queue

# binary tree
class BinaryTree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# binary search tree
class BST(BinaryTree):
	def __init__(self, data=None):
		BinaryTree.__init__(self, data)
	def search(self, key):
		if self.data == None:
			return None
		if key == self.data:
			return self
		if key < self.data:
			return self.left.search(key)
		if key > self.data:
			return self.right.search(key)			
	def insert(self, data):
		if self.data == None:
			self = BST(data)
			return self
		if data == self.data:
			raise Exception("Value already exists within tree")
		if data < self.data:
			if self.left == None:
				self.left = BST(data)
				return self.left
			else:
				return self.left.insert(data)
		if data > self.data:
			if self.right == None:
				self.right = BST(data)
				return self.right
			else:
				return self.right.insert(data)
	def insertTree(self, root):
		if self.data == None:
			self = root
			return root
		if root.data == self.data:
			raise Exception("Value already exists within tree")
		if root.data < self.data:
			if self.left == None:
				self.left = root
			else:
				return self.left.insertTree(root)
		if root.data > self.data:
			if self.right == None:
				self.right = root
			else:
				return self.right.insertTree(root)			
	def remove(self, key):
		if self.data == None:
			return self
		if key == self.data:
			if self.left != None and self.right != None:
				p = self
				n = p.right
				while n.left != None:
					p = n
					n = n.left
				if n.right != None:
					p.left = n.right
				else:
					p.left = None
				n.left = self.left
				n.right = self.right
				return n
			elif self.left != None:
				return self.left
			elif self.right != None:
				return self.right
		elif key < self.data:
			if self.left != None:
				self.left = self.left.remove(key)
		elif key > self.data:
			if self.right != None:
				self.right = self.right.remove(key)
		return self

# height
def height(root):
	if root == None:
		return 0
	return (1+max(height(root.left), height(root.right)))


# AVL
def isAVL(root):
	if root == None or root.data == None:
		return True
	if isAVL(root.left) and isAVL(root.right):
		return (abs(height(root.left)-height(root.right)) <= 1)
	return False

# breadth first search
def BFS(root, key):
	q = Queue.Queue()
	q.put(root)
	while (not q.empty()):
		n = q.get()
		print n.data, # test
		if (n.data == key):
			return n
		if (n.left != None):
			q.put(n.left)
		if (n.right != None):
			q.put(n.right)
	return None

# iterative depth first search
def DFS(root, key):
	q = Queue.LifoQueue()
	q.put(root)
	while (not q.empty()):
		n = q.get()
		print n.data, # test
		if (n.data == key):
			return n
		if (n.right != None):
			q.put(n.right)
		if (n.left != None):
			q.put(n.left)
	return None

# recursive depth first search
def recursiveDFS(root, key):
	print root.data, # test
	if root.data == key:
		return root
	if root.left != None:
		left = recursiveDFS(root.left, key)
		if left != None:
			return left
	if root.right != None:
		right = recursiveDFS(root.right, key)
		if right != None:
			return right
	return None


# data structure and algorithms testing

root = BinaryTree(0)
root.left = BinaryTree(1)
root.right = BinaryTree(2)
root.left.left = BinaryTree(3)
root.left.right = BinaryTree(4)
root.right.left = BinaryTree(5)
root.right.right = BinaryTree(6)
root.left.left.left = BinaryTree(7)
root.left.left.right = BinaryTree(8)
root.left.right.left = BinaryTree(9)
root.left.right.right = BinaryTree(10)
root.right.left.left = BinaryTree(11)
root.right.left.right = BinaryTree(12)
root.right.right.left = BinaryTree(13)
root.right.right.right = BinaryTree(14)

n = BFS(root, 10)
print "Found:", n.data
n = DFS(root, 10)
print "Found:", n.data
n = recursiveDFS(root, 10)
print "Found:", n.data

bstroot = BST(7)
bstroot.insert(4)
bstroot.insert(10)
bstroot.insert(2)
bstroot.insert(9)
bstroot.insert(6)
bstroot.insert(12)
bstroot.insert(3)
bstroot.insert(13)
bstroot.insert(1)
bstroot.insert(8)
bstroot.insert(5)
bstroot.insert(11)
bstroot.insert(0)
bstroot = bstroot.remove(1)
n = BFS(bstroot, 13)
print "BST Found:", n.data

print "isAVL1: ", isAVL(bstroot)
bstroot.insert(-1)
bstroot.insert(-2)
print "isAVL2: ", isAVL(bstroot)
