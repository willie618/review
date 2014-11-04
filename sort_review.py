#!/usr/bin/python

def bubbleSort(x):
	swapped = True
	while swapped:
		swapped = False
		i = 0
		for i in range(0, len(x)-1):
			if x[i] > x[i+1]:
				(x[i], x[i+1]) = (x[i+1], x[i])
				swapped  = True
	return x

def selectionSort(x):
	i = 0
	min = i
	while i < len(x):
		for j in range(i+1, len(x)):
			if x[j] < x[min]:
				min = j
		(x[i], x[min]) = (x[min], x[i])
		i = i + 1
		min = i
	return x

def insertionSort(x):
	for i in range(1, len(x)):
		j = i
		while j > 0 and x[j] < x[j-1]:
			(x[j-1], x[j]) = (x[j], x[j-1])
			j = j - 1
	return x

def mergeSort(x):
	if len(x) < 2:
		return x
	a = x[0:len(x)/2]
	b = x[len(x)/2:len(x)]
	a = mergeSort(a)
	b = mergeSort(b)
	c = []
	while len(a) > 0 or len(b) > 0:
		if len(a) == 0:
			c.append(b[0])
			del b[0]
		elif len(b) == 0:
			c.append(a[0])
			del a[0]					
		elif a[0] <= b[0]:
			c.append(a[0])
			del a[0]
		elif a[0] > b[0]:
			c.append(b[0])
			del b[0]
	return c

def quickSort(x):
	if len(x) < 2:
		return x
	pivot = x[len(x)-1]
	i = 0
	j = len(x)-2
	while i <= j:
		if x[i] > pivot and x[j] < pivot:
			(x[i], x[j]) = (x[j], x[i])
			i = i + 1
			j = j - 1
		elif x[i] > pivot:
			j = j - 1
		elif x[j] < pivot:
			i = i + 1
		else:
			i = i + 1
			j = j - 1
	(x[i], x[len(x)-1]) = (x[len(x)-1], x[i])
	x[0:i] = quickSort(x[0:i])
	x[i+1:len(x)] = quickSort(x[i+1:len(x)])
	return x

def countingSort(x):
	neg = []
	pos = []
	if min(x) < 0:
		neg = [0]*(abs(min(x))+1)
	if max(x) > 0:
		pos = [0]*(max(x)+1)
	for i in x:
		if i < 0:
			neg[abs(i)] = neg[abs(i)] + 1
		else:
			pos[i] = pos[i] + 1
	y = []
	for i in range(len(neg)-1, -1, -1):
		while neg[i] > 0:
			y.append((-1)*i)
			neg[i] = neg[i] - 1
	for	i in range(0, len(pos)):
		while pos[i] > 0:
			y.append(i)
			pos[i] = pos[i] - 1
	x = y
	return x

def radixSort(x):
	neg = []
	pos = []
	y = x
	if min(x) < 0:
		for i in x:
			if i < 0:
				neg.append(abs(i))
			else:
				pos.append(i)
		neg = radixSort(neg)
		for i in range(0, len(neg)):
			neg[i] = (-1)*neg[i]
		neg.reverse()
		y = pos
	m = max(x)
	radix = 1
	buckets = [list() for i in range(10)]
	while m / radix > 0:
		for i in y:
			digit = (i / radix) % 10
			buckets[digit].append(i)
		y = []
		for i in buckets:
			for j in i:
				y.append(j)
		buckets = [list() for i in range(10)]
		radix = radix * 10
	if len(neg) > 0:
		x = neg+y
	else:
		x = y
	return x

def buildMinHeap(x, index=0):
	left = 2*index+1
	right = 2*index+2
	swapped = True
	while swapped:
		swapped = False
		if left < len(x):
			x = buildMinHeap(x, left)
		if right < len(x):
			x = buildMinHeap(x, right)
		if left < len(x) and x[index] > x[left]:
			(x[index], x[left]) = (x[left], x[index])
			swapped = True
		if right < len(x) and x[index] > x[right]:
			(x[index], x[right]) = (x[right], x[index])
			swapped = True
	return x

def heapify(x, index=0):
	if index == 0:
		x[index] = x[len(x)-1]	
		x = x[0:len(x)-1]
	left = 2*index+1
	right = 2*index+2
	if left < len(x) and x[index] > x[left]:
		(x[index], x[left]) = (x[left], x[index])
		x = heapify(x, left)
	if right < len(x) and x[index] > x[right]:
		(x[index], x[right]) = (x[right], x[index])
		x = heapify(x, right)
	return x

def heapSort(x):
	h = buildMinHeap(x)
	y = []
	while len(h) > 0:
		y.append(h[0])
		h = heapify(h)
	x = y
	return x

x = [2,8888,-6,-44,1,-999,30,50,777]
b = bubbleSort(x)
x = [2,8888,-6,-44,1,-999,30,50,777]
s = selectionSort(x)
x = [2,8888,-6,-44,1,-999,30,50,777]
i = insertionSort(x)
x = [2,8888,-6,-44,1,-999,30,50,777]
m = mergeSort(x)
x = [2,8888,-6,-44,1,-999,30,50,777]
q = quickSort(x)
x = [2,8888,-6,-44,1,-999,30,50,777]
c = countingSort(x)
x = [2,8888,-6,-44,1,-999,30,50,777]
r = radixSort(x)
x = [2,8888,-6,-44,1,-999,30,50,777]
h = heapSort(x)
x = [2,8888,-6,-44,1,-999,30,50,777]
print "x", x
print "b", b
print "s", s
print "i", i
print "m", m
print "q", q
print "c", c
print "r", r
print "h", h
