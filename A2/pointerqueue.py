# Creating a class in order to store pointer data
class Node:
	def __init__(self):
		self.data = None
		self.nxt = None
	
	def __str__(self):
		return str(self.data)

# Creating a class to keep information about a pointer
class pointer_queue:
	def __init__(self):
		self.front = None
		self.current = None

# This method makes the queue empty
def MAKENULL(Q):
	# make null by returning pointer as a new pointer
	Q = pointer_queue()
	return Q

# This method returns the front element of the queue
def FRONT(Q):
	return Q.front

# This method inserts a given element to the end of the queue
def ENQUEUE(x,Q):
	end = Node()
	end.data = x
	
	if Q.front is None:
		Q.front = end
		Q.current = end

	else:
		t1 = Q.front	
		while t1.nxt:
			t1 = t1.nxt
		t1.nxt = end 
		Q = t1
	return

# This method deletes the first element
def DEQUEUE(Q):
	Q.front = Q.front.nxt
	Q.current = Q.front
	return

# This method returns TRUE if the queue is empty
def EMPTY(Q):
	if Q.front is None:
		return True
	else:
		return False

# This method prints the queue
def PRINT(Q):
	t1 = FRONT(Q);
	if t1 is None:
		print
	else:
		while t1:
			print t1
			t1 = t1.nxt
		print
