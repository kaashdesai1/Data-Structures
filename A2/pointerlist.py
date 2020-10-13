# Creating a class node to store info in pointer
class Node:
	def __init__(self):
		self.data = None
		self.nxt = None

	def __str__(self):
		return str(self.data)

# Class to keep pointer information
class ptr_list:
	def __init__(self):
		self.head = None
		self.current = None
	def __len__(self):
		return len(self)

# This method returns first item in list
def FIRST(L):
	return L.head

# This method returns last item in a list
def END(L):
	if L.head is None and L.current is None:
		return None
	else:
		t1 = L.head
		while t1.nxt:
			t1 = t1.nxt
		return t1


# This method returns element at a given position of list
def RETRIEVE(p,L):

	t1 = L.head

	for n in range(0, p):
		if t1.nxt  != None :
			t1 = t1.nxt
	return t1


# This method returns the position of a given element in list
def LOCATE(x,L):
	p = 0
	t1 = L.head
	while t1:
		if t1.data == x:
			return p
		else:
			p = p + 1
			t1 = t1.nxt

	return None

# This method returns the next element following a given position
def NEXT(p,L):
	t1 = L.head
	loc = 0
	while t1:
		if loc == (p+1):
			return t1
		else:
			t1 = t1.nxt
		loc = loc + 1
	return None

def NEXT_TREE(p):
		return p.nxt
	
def PREVIOUS(p,L):
	t1 = L.head
	loc = 0
	while t1 :
		if loc  == (p-1) :
			return t1
		else:
			t1 = t1.nxt
		loc = loc + 1
	return None

def INSERT(x,p,L):

	node = Node()
	node.data = x

	if p is None:
		node.nxt = None
		L.head = node
		L.current = L.head
		return
	elif (p == 0) or (p == FIRST(L) and FIRST(L) != END(L)):
		node.nxt = L.head
		L.head = node
		L.current = L.head
		return
	else:
	
		if L.head is None:
			L.head = node
			L.current = node
	
		else:
			t1 = FIRST(L)
			while t1 and p > 1:
				t1 = t1.nxt
				p = p - 1
			if t1:
				node.nxt = t1.nxt
				t1.nxt = node
		return

# This method makes a list NULL
def MAKENULL(L):
	L = ptr_list()
	return L

def DELETE(p,L):
	t1 = L.head
	if p == 0:
		L.head = t1.nxt

	elif p == END(L):
		if t1.nxt == None:
			L = MAKENULL(L)
		else:
			while (t1.nxt).nxt :
				t1 = t1.nxt
			t1.nxt = None
	else:
		while t1 and (p - 1) > 0:
				t1 = t1.nxt
				p = p - 1
		before = t1
		if t1 is not None:
			if t1.nxt is not None:
				after = t1.nxt
		else:
			after = None
		if before is not None:
			if before.nxt is not None:
				before.nxt = after.nxt
	L.current = L.head

# This method prints the list
def PRINT(L):
	t1 = FIRST(L)
	if t1 is None:
		print "list is empty"
	else:
		while t1:
			print t1,
			t1 = t1.nxt
	print
