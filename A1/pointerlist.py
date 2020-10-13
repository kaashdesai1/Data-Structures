class Node:
	def __init__(self):
		self.data = None
		self.nxt = None

	def __str__(self):
		return str(self.data)

class pointer_list:
	def __init__(self):
		self.head = None
		self.current = None
	def __len__(self):
		return len(self)

# This method returns the 1st item in the pointer list
def FIRST(L):
	return L.head


# This method returns the last item in the pointer list
def END(L):
	if (L.head is None and l.current is None):
		return None
	else:
		t1 = L.head
		while t1.nxt:
			t1 = t1.nxt
		return t1


# This method returns an element at a given position of the pointer list
def RETRIEVE(p, L):
	t1 = L.head

	for n in range(0, p):
		if t1.nxt  != None :
			t1 = t1.nxt
	return t1.data


# This method returns the position of a given element in the pointer list
def LOCATE(x, L):
	p = 0
	t1 = L.head
	
	while t1:
		if t1.data == x:
			return p
		else:
			p = p + 1
			t1 = t1.nxt
	return None


# This method returns the next element following a given position in the pointer list
def NEXT(p, L):
	t1 = L.head
	l = 0
	
	while t1:
		if l == (p+1):
			return t1
		else:
			t1 = t1.nxt
		l = l + 1
	return None


# This method returns the previous element preceding a given position in the pointer list
def PREVIOUS(p, L):
	t1 = L.head
	l = 0
	while t1:
		if l  == (p-1) :
			return t1
		else:
			t1 = t1.nxt
		l = l + 1
	return None


# This method inserts an element at a given position of the pointer list
def INSERT(x, p, L):
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
			
			while (t1 and p > 1):
				t1 = t1.nxt
				p = p - 1
			if t1:
				
				node.nxt = t1.nxt
				t1.nxt = node
		return


# This method makes a list null and returns the end of the pointer list
def MAKENULL(L):
	L = pointer_list()
	return L


# This method deletes an element at a given position of the pointer list
def DELETE(p, L):
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


# This method returns the list of values, instead of just the hex pointer
def PRINT(L):
	t1 = FIRST(L)
	if t1 is None:
		print "This list is empty"
	else:
		while t1:
			print t1
			t1 = t1.nxt
	print

def main():
	
	# Testing out INSERT
	print "TEST 1. INSERT \nExpected Result: \n1\n2\n3\n4\n5\n"
	my_list = pointer_list()
	INSERT(1,0, my_list)
	INSERT(2,1, my_list)
	INSERT(3,2, my_list)
	INSERT(4,3, my_list)
	INSERT(5,4, my_list)
	print "Actual Result: \n", PRINT(my_list), "\n"	

	# Testing out DELETE
	print "TEST 2. DELETE \nExpected result: \n1\n3\n4\n5\n"
	DELETE(1, my_list)
	print "Actual Result: \n", PRINT(my_list), "\n"

	# Testing out FIRST
	print "TEST 3. FIRST \nExpected result: 1"
	print "Actual Result: ", FIRST(my_list), "\n"

	# Testing out END
	print "TEST 4. END \nExpected result: 5"
	print "Actual Result: ", END(my_list), "\n"

	# Testing out NEXT
	print "TEST 5. NEXT \nExpected result: 5"
	print "Actual Result: ", NEXT(2, my_list), "\n"

	# Testing out PREVIOUS
	print "TEST 6. PREVIOUS \nExpected result: 3"
	print "Actual Result: ", PREVIOUS(2, my_list), "\n"

	# Testing out LOCATE
	print "TEST 7. LOCATE \nExpected result: 3"
	print "Actual Result: ", LOCATE(5, my_list), "\n"

	# Testing out RETRIEVE
	print "TEST 8. RETRIEVE \nExpected result: 4"
	print "Actual Result: ", RETRIEVE(2, my_list), "\n"

	# Testing out MAKENULL
	print "TEST 9. MAKENULL \nExpected result: This list is empty"
	my_list = MAKENULL(my_list)
	print "Actual Result: ", PRINT(my_list)


main()
