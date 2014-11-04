#!/usr/bin/python
import Queue
from math import floor, log

# binary tree
class BinaryTree:
	def __init__(self, data=None):
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
				return self
			else:
				self.left.insert(data)
				return self
		if data > self.data:
			if self.right == None:
				self.right = BST(data)
				return self
			else:
				self.right.insert(data)
				return self
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
				if p != self:
					if n.right != None:
							p.left = n.right
					else:
						p.left = None
					n.right = self.right
				n.left = self.left
				return n
			elif self.left != None:
				return self.left
			elif self.right != None:
				return self.right
			else:
				self.data = None
				return self
		elif key < self.data:
			if self.left != None:
				self.left = self.left.remove(key)
		elif key > self.data:
			if self.right != None:
				self.right = self.right.remove(key)
		return self

# AVL tree
class AVL(BinaryTree):
	def __init__(self, data=None):
		BinaryTree.__init__(self, data)
	def rotate(self):
		hd = [heightDiff(self)]
		if abs(hd[0]) <= 1:
			return self
		elif hd[0] > 1:
			child = self.left
		elif hd[0] < -1:
			child = self.right
		hd.append(heightDiff(child))
		# LL
		if hd[0] > 1 and hd[1] > 0:
			self.left = child.right
			child.right = self
			return child
		# LR
		elif hd[0] > 1 and hd[1] < 0:
			grandchild = child.right
			child.right = grandchild.left
			self.left = grandchild.right
			grandchild.left = child
			grandchild.right = self
			return grandchild
		# RL
		elif hd[0] < -1 and hd[1] > 0:
			grandchild = child.left
			child.left = grandchild.right
			self.right = grandchild.left
			grandchild.left = self
			grandchild.right = child
			return grandchild
		# RR
		elif hd[0] < -1 and hd[1] < 0:
			self.right = child.left
			child.left = self
			return child
		return self
	def balance(self):
		if height(self) < 3:
			return self
		if self.left != None:
			self.left = self.left.balance()
		if self.right != None:
			self.right = self.right.balance()
		self = self.rotate()
		return self
	def insert(self, data):
		if data == None:
			return self
		p = None
		n = self
		while n != None:
			if data == n.data:
				raise Exception("Value already exists within tree")
			elif data < n.data:
				p = n
				n = n.left
			elif data > n.data:
				p = n
				n = n.right
		n = AVL(data)
		if data < p.data:
			p.left = n
		elif data > p.data:
			p.right = n
		self = self.balance()
		return self
	def insertTree(self, root):
		while root != None and root.data != None:
			data = root.data
			self = self.insert(data)
			root = root.remove(data)
		return self
	def remove(self, key):
		if self.data == None:
			return self
		if key == self.data:
			if self.left != None and self.right != None:
				if heightDiff(self) < 0:
					p = self
					n = p.right
					while n.left != None:
						p = n
						n = n.left
					if p != self:
						if n.right != None:
							p.left = n.right
						else:
							p.left = None
						n.right = self.right
					n.left = self.left
					n = n.balance()
					return n
				else:
					p = self
					n = p.left
					while n.right != None:
						p = n
						n = n.right
					if p != self:
						if n.left != None:
							p.right = n.left
						else:
							p.right = None
						n.left = self.left
					n.right = self.right
					n = n.balance()
					return n
			elif self.left != None:
				return self.left
			elif self.right != None:
				return self.right
			else:
				self.data = None
				return self				
		elif key < self.data:
			if self.left != None:
				self.left = self.left.remove(key)
		elif key > self.data:
			if self.right != None:
				self.right = self.right.remove(key)
		self = self.balance()
		return self

# height
def height(root):
	if root == None:
		return 0
	return (1+max(height(root.left), height(root.right)))

# height difference
def heightDiff(root):
	return height(root.left) - height(root.right)

# node count
def nodeCount(root):
	q = Queue.Queue()
	count = 0
	if root == None or root.data == None:
		return count
	q.put(root)
	while (not q.empty()):
		n = q.get(root)
		count = count + 1
		if n.left != None:
			q.put(n.left)
		if n.right != None:
			q.put(n.right)
	return count

# verify height balanced
def isHeightBalanced(root):
	if root == None or root.data == None:
		return True
	h = height(root)
	c = nodeCount(root)
	return h <= floor(log(c, 2) + 1)

# verify AVL
def isAVL(root):
	if root == None or root.data == None:
		return True
	if isAVL(root.left) and isAVL(root.right):
		return abs(heightDiff(root)) <= 1
	return False

# test function
def printTree(root):
	q = Queue.Queue()
	h = Queue.Queue()
	q.put(root)
	h.put(0)
	currentHeight = 0
	while (not q.empty()):
		n = q.get()
		if h.get() > currentHeight:
			currentHeight = currentHeight + 1
			print ""
		print n.data, # test
		if (n.left != None):
			q.put(n.left)
			h.put(currentHeight+1)
		if (n.right != None):
			q.put(n.right)
			h.put(currentHeight+1)
	print ""

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
bstroot.insert(-1)
bstroot.insert(-2)

avlroot = AVL(100)
avlroot = avlroot.insert(200)
avlroot = avlroot.insert(300)
avlroot = avlroot.insert(400)
avlroot = avlroot.insert(500)
avlroot = avlroot.insert(600)
avlroot = avlroot.insert(700)
avlroot = avlroot.insert(800)
avlroot = avlroot.insert(900)
avlroot = avlroot.insertTree(bstroot)

printTree(avlroot)
print "isAVL:", isAVL(avlroot)
print "height:", height(avlroot)
print "heightDiff:", heightDiff(avlroot)

while(avlroot != None and avlroot.data != None):
	data = avlroot.data
	avlroot = avlroot.remove(data)
	print "==Line Break=="
#	print "height:", height(avlroot)
#	print "heightDiff:", heightDiff(avlroot)
#	print "count:", nodeCount(avlroot)
#	print "isHeightBalanced:", isHeightBalanced(avlroot)
#	print "isAVL:", isAVL(avlroot)
	printTree(avlroot)
print "Done"
