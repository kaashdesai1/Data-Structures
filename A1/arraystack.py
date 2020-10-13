# This method returns the top element in the stack
def TOP(S):
	return S[0]


# This method returns and deletes the element at the top of the stack
def POP(S):
	top = S[0]
	del S[0]
	return top


# This method inserts the element "x" at the top of the stack
def PUSH(x,S):
	t1 = S[:]
	S = MAKENULL(S)
	S.append(x)
	for i in t1:
		S.append(i)
	return S


# This method returns "True" if the stack is empty and "False" if it is not empty
def EMPTY(S):
	if len(S) == 0:
		return True
	else:
		return False


# This method clears the stack
def MAKENULL(S):
	S = []
	return S

def main():
	
	# Testing out PUSH
	print "TEST 1. PUSH \nExpected Result: [1, 2, 3, 4, 5]"
	my_stack = []
	my_stack = PUSH(5,my_stack)
	my_stack = PUSH(4,my_stack)
	my_stack = PUSH(3,my_stack)
	my_stack = PUSH(2,my_stack)
	my_stack = PUSH(1,my_stack)
	print "Actual Result: ", my_stack, "\n"

	# Testing out TOP
	print "TEST 2. TOP \nExpected result: 1"
	print "Actual Result: ", TOP(my_stack), "\n"

	# Testing out POP
	print "TEST 3. POP \nExpected result: 1"
	print "Actual Result: ", POP(my_stack), "\n"

	# Testing out PUSH
	print "TEST 4. PUSH \nExpected result: [260, 2018, 666, 2, 3, 4, 5] "
	my_stack = PUSH(666, my_stack)
	my_stack = PUSH(2018, my_stack)
	my_stack = PUSH(260, my_stack)
	print "Actual Result: ", my_stack, "\n"

	# Testing out EMPTY
	print "TEST 5. EMPTY \nExpected result: False"
	print "Actual Result: ", EMPTY(my_stack), "\n"

	# Testing out MAKENULL
	print "TEST 6. MAKENULL \nExpected result: []"
	my_stack = MAKENULL(my_stack)
	print "Actual Result: ", my_stack, "\n"


main()
