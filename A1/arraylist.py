def FIRST(L):
	return L[0]


# This method returns the last item in the list
def END(L):
	end = len(L) - 1
	return L[end]


# This method returns an element at a given position of the list
def RETRIEVE(p, L):
	end = len(L) - 1

	if p <0 :
		print ("Oops... Position needs to be from 0 to %d", end)
	elif p > end :
		print ("Oops... Position needs to be from 0 to %d", end)
	else:
		return L[p]


# This method returns the position of a given element in the list
def LOCATE(x,L):
	p = 0
	for i in L:
		if i == x:
			return p
			break
		p = p + 1
	else:
		return END(L)


# This method returns the next element following a given position
def NEXT(p, L):

	if (p+1) > (len(L)-1) :
		return END(L)
	else:
		return L[p+1]


# This method returns the previous element preceding a given position
def PREVIOUS(p, L):
	if p > 0:
		return L[p-1]
	else:
		return L[0]


# This method inserts an element at a given position of the list
def INSERT(x, p, L):
	if p >= (len(L)):
		L.append(x)
	else:
		t1 = L[:p]
		t2 = [x]
		t3 = L[p:]
		L = MAKENULL(L)
		L.extend(t1)
		L.extend(t2)
		L.extend(t3)


# This method deletes an element at a given position of the list
def DELETE(p, L):
	t1 = L[:p]
	t2 = L[(p+1):]
	L = MAKENULL(L)
	L.extend(t1)
	L.extend(t2)


# This method makes a list null and returns the end of the list
def MAKENULL(L):
	del L[:]
	return L


def main():

	# Testing out INSERT
	print "TEST 1. INSERT \nExpected Result: [1, 2, 3, 4, 5]"
	my_list = []
	INSERT(1,0, my_list)
	INSERT(2,1, my_list)
	INSERT(3,2, my_list)
	INSERT(4,3, my_list)
	INSERT(5,4, my_list)
	print "Actual Result: ", my_list, "\n"

	# Testing out FIRST
	print "TEST 2. FIRST \nExpected result: 1"
	print "Actual Result: ", FIRST(my_list), "\n"

	# Testing out END
	print "TEST 3. END \nExpected result: 5"
	print "Actual Result: ", END(my_list), "\n"

	# Testing out LOCATE
	print "TEST 4. LOCATE \nExpected result: 4"
	print "Actual Result: ", LOCATE(5, my_list), "\n"

	# Testing out RETRIEVE
	print "TEST 5. RETRIEVE \nExpected result: 3"
	print "Actual Result: ", RETRIEVE(2, my_list), "\n"

	# Testing out DELETE
	print "TEST 6. DELETE \nExpected result: [1, 3, 4, 5]"
	DELETE(1, my_list)
	print "Actual Result: ", my_list, "\n"

	# Testing out NEXT
	print "TEST 7. NEXT \nExpected result: 5"
	print "Actual Result: ", NEXT(2, my_list), "\n"

	# Testing out PREVIOUS
	print "TEST 8. PREVIOUS \nExpected result: 3"
	print "Actual Result: ", PREVIOUS(2, my_list), "\n"

	# Testing out MAKENULL
	print "TEST 9. MAKENULL \nExpected result: []"
	print "Actual Result: ", MAKENULL(my_list), "\n"


main()
