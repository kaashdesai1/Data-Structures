import pointerlist

# Creating a class for a tree
class tree():
	def __init__(self):
		self.children = None
		self.root = None

# This method makes the tree NULL
def MAKENULL(T):
	T = tree()
	T.children = [None]*100
	return T	

# This method returns the parent in a tree
def PARENT(n,T):
	if T.children[T.root] == n:
		return None
	else:
		for i in range(0, len(T.children)):
			
			if T.children[i] is not None:
				pos = pointerlist.LOCATE(n.data, T.children[i])
			
				if pos != -1 and pos != 0 and pos is not None:
					return pointerlist.FIRST(T.children[i])
		return None


# This method returns the leftmost child
def LEFTMOST_CHILD(n,T):
	for i in range(len(T.children)):
		if T.children[i] is not None:
			
			if LABEL(pointerlist.FIRST(T.children[i]),T) == LABEL(n,T):
				return pointerlist.NEXT_TREE(pointerlist.FIRST(T.children[i]))
	return None


# This method returns the right sibling in a tree
def RIGHT_SIBLING(n,T):
	
	for i in range(0, len(T.children)):
		if T.children[i] is not None:
			pos = pointerlist.LOCATE(n.data, T.children[i])
			if pos != 0 and pos != -1 and pos is not None:
				return pointerlist.NEXT_TREE(pointerlist.RETRIEVE(pos, T.children[i]))
	return None


# This method returns the lable of a node
def LABEL(n,T):
	return n.data
	for i in range(0, len(T.children)):
		if n == T.children[i]:
			t = T.children[i]
			return t.data

# This method returns the node that is the root of a given tree
def ROOT(T):

	return pointerlist.FIRST(T.children[T.root])

# This method creates new nodes with given label and roots of trees (v - label)
def CREATE0(v):
	
	new_tree = tree()
	new_tree = MAKENULL(new_tree)
	
	new_tree.children[v] = pointerlist.ptr_list()
	
	new_tree.root = v
	
	pointerlist.INSERT(v, pointerlist.END(new_tree.children[v]), new_tree.children[v])
	return new_tree

# This method creates new tree from label and tree
def CREATE1(v, T):

	new_tree = tree()
	new_tree = MAKENULL(new_tree)

	for i in range(0, len(T.children)):
		if T.children[i] is not None:
			new_tree.children[i] = T.children[i]

	new_tree.children[v] = pointerlist.ptr_list()
	new_tree.root = v
	pointerlist.INSERT(v, pointerlist.END(new_tree.children[v]), new_tree.children[v])
	pointerlist.INSERT(T.root, pointerlist.END(new_tree.children[v]), new_tree.children[v])

	return new_tree


# This method is same as CREATE1 but with 2 trees
def CREATE2(v, T1, T2):
	new_tree = tree()
	new_tree = MAKENULL(new_tree)
	
	
	for i in range(0, len(T1.children)):
		if T1.children[i] is not None:
			new_tree.children[i] = T1.children[i]
		elif T2.children[i] is not None:
			new_tree.children[i] = T2.children[i]

	new_tree.children[v] = pointerlist.ptr_list()
	new_tree.root = v

	pointerlist.INSERT(v, pointerlist.END(new_tree.children[v]), new_tree.children[v])
	pointerlist.INSERT(T2.root, pointerlist.END(new_tree.children[v]), new_tree.children[v])
	pointerlist.INSERT(T1.root, pointerlist.END(new_tree.children[v]), new_tree.children[v])
	
	return new_tree


# This method is same as other CREATE functions but with 3 trees
def CREATE3(v, T1, T2, T3):
	new_tree = tree()
	new_tree = MAKENULL(new_tree)
	
	for i in range(0, len(T1.children)):
		if T1.children[i] is not None:
			new_tree.children[i] = T1.children[i]
		elif T2.children[i] is not None:
			new_tree.children[i] = T2.children[i]
		elif T3.children[i] is not None:
			new_tree.children[i] = T3.children[i]
	
	new_tree.children[v] = pointerlist.ptr_list()
	new_tree.root = v
	pointerlist.INSERT(v, pointerlist.END(new_tree.children[v]), new_tree.children[v])
	pointerlist.INSERT(T3.root, pointerlist.END(new_tree.children[v]), new_tree.children[v])
	pointerlist.INSERT(T2.root, pointerlist.END(new_tree.children[v]), new_tree.children[v])
	pointerlist.INSERT(T1.root, pointerlist.END(new_tree.children[v]),new_tree.children[v])

	return new_tree


# This method prints a tree in an order
def PRINT(T):
	for i in range(0, len(T.children)):
		if T.children[i] is not None:
			print i, "-",  
			pointerlist.PRINT(T.children[i])
