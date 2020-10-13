# This method returns the 1st item in the list
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


def PRINT(L):
	print L

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
