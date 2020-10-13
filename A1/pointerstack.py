# Description: 	This program implements the following basic datatypes
# 			 	in the pointer stack: TOP, POP, PUSH, EMPTY, MAKENULL


class Node:
	def __init__(self):
		self.data = None
		self.n3xt = None
	
	def __str__(self):
		return str(self.data)

class pointer_stack:
	def __init__(self):
		self.top = None

# This method returns the top element in the stack
def TOP(S):
	return S.top

# This method returns and deletes the element at the top of the stack
def POP(S):
	S.top = S.top.n3xt
	return

# This method inserts the element "x" at the top of the stack
def PUSH(x,S):
	t1 = Node()
	t1.data = x
	t1.n3xt = S.top
	S.top = t1
	return

# This method returns "True" if the stack is empty and "False" if it is not empty
def EMPTY(S):
	if S.top is None:
		return True
	else:
		return False

# This method clears the stack
def MAKENULL(S):
	S = pointer_stack()
	return S

# This method returns the stack, instead of just the hex pointer
def PRINT(S):
	t1 = TOP(S)
	if t1 is None:
		print
	else:
		while t1:
			print t1
			t1 = t1.n3xt

def main():

	# Testing out PUSH
	print "TEST 1. PUSH \nExpected Result: \n1\n2\n3\n4\n5\n"
	my_stack = pointer_stack()
	PUSH(5,my_stack)
	PUSH(4,my_stack)
	PUSH(3,my_stack)
	PUSH(2,my_stack)
	PUSH(1,my_stack)
	print "Actual Result: \n", PRINT(my_stack), "\n"

	# Testing out TOP
	print "TEST 2. TOP \nExpected result: 1"
	print "Actual Result: ", TOP(my_stack), "\n"

	# Testing out POP
	print "TEST 3. POP \nExpected result: \n2\n3\n4\n5\n"
	POP(my_stack)
	print "Actual Result: \n", PRINT(my_stack), "\n"

	# Testing out EMPTY
	print "TEST 4. EMPTY \nExpected result: False"
	print "Actual Result: ", EMPTY(my_stack), "\n"

	# Testing out MAKENULL
	print "TEST 5. MAKENULL \nExpected result: nothing"
	my_stack = MAKENULL(my_stack)
	print "Actual Result: ", PRINT(my_stack), "\n"


main()
