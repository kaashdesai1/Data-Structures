# Creating a class for three nodes
class Node_Tree():
	def __init__(self):
		self.label = None
		self.left_child = None
		self.right_sibling = None
		self.parent = None

	def __str__(self):
		return str(self.label)


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
	return T.children[n.parent]

# This method returns the leftmost child
def LEFTMOST_CHILD(n,T):
	if n.left_child == None:
		return None
	else:
		return T.children[n.left_child]
	print "Ooops... ", n, " is not a part of given tree!"


# This method returns the right sibling in a tree
def RIGHT_SIBLING(n,T):
	if n.right_sibling is None:
		return None
	else:
		return T.children[n.right_sibling]
	print "Error: ", n, "is not a part of given tree!"


# This method returns the lable of a node
def LABEL(n,T):
	return n.label

# This method returns the node that is the root of a given tree
def ROOT(T):
	return T.children[T.root]


# This method creates new nodes with given label and roots of trees (v - label)
def CREATE0(v):
	
	new_tree = tree()
	new_tree = MAKENULL(new_tree)	
	
	new_tree.children[v] = Node_Tree()
	new_tree.children[v].label = v

	new_tree.root = v
	return new_tree	


# This method creates new tree from label and tree
def CREATE1(v, T):
	
	new_tree = tree()
	new_tree = MAKENULL(new_tree)
	
	for i in range(0, len(T.children)):
		if T.children[i] is not None:
			new_tree.children[i] = T.children[i]
	
	new_tree.children[v] = Node_Tree()
	new_tree.children[T.root] = Node_Tree()
	new_tree.children[v].label = v
	new_tree.children[v].left_child = T.root
	new_tree.children[v].right_sibling = None
	new_tree.children[T.root].label = T.root
	new_tree.children[T.root].right_sibling = None
	new_tree.children[T.root].parent = v
	
	new_tree.root = v
	return new_tree

# This method is same as CREATE1 but with 2 trees
def CREATE2(v, T1, T2):
	new_tree = tree()
	new_tree = MAKENULL(new_tree)
	

	for i in range(0, 100):
		if T1.children[i] is not None:
			new_tree.children[i] = T1.children[i]
		elif T2.children[i] is not None:
			new_tree.children[i] = T2.children[i]

	new_tree.children[v] = Node_Tree()
	new_tree.children[T1.root] = Node_Tree()
	new_tree.children[T2.root] = Node_Tree()
	new_tree.children[v].label = v
	new_tree.children[v].left_child = T1.root
	new_tree.children[v].right_sibling = None
	new_tree.children[T1.root] = T1.children[T1.root]
	new_tree.children[T1.root].right_sibling = T2.root
	new_tree.children[T1.root].parent = v
	new_tree.children[T2.root] = T2.children[T2.root]
	new_tree.children[T2.root].parent = v
	new_tree.children[T2.root].right_sibling = None

	new_tree.root = v
	
	return new_tree


# This method is same as other CREATE functions but with 3 trees
def CREATE3(v, T1, T2, T3):
	new_tree = tree()
	new_tree = MAKENULL(new_tree)
	for i in range(0, 100):
		if T1.children[i] is not None:
			new_tree.children[i] = T1.children[i]
		elif T2.children[i] is not None:
			new_tree.children[i] = T2.children[i]
		elif T3.children[i] is not None:
			new_tree.children[i] = T3.children[i]

	new_tree.children[v] = Node_Tree()
	new_tree.children[T1.root] = Node_Tree()
	new_tree.children[T2.root] = Node_Tree()
	new_tree.children[T3.root] = Node_Tree()
	new_tree.children[v].label = v
	new_tree.children[v].left_child = T1.root
	new_tree.children[v].right_sibling = None
	new_tree.children[T1.root] = T1.children[T1.root]
	new_tree.children[T1.root].right_sibling = T2.root
	new_tree.children[T1.root].parent = v
	new_tree.children[T2.root] = T2.children[T2.root]
	new_tree.children[T2.root].right_sibling = T3.root
	new_tree.children[T2.root].parent = v
	new_tree.children[T3.root] = T3.children[T3.root]
	new_tree.children[T3.root].parent = v	
	new_tree.children[T3.root].right_sibling = None

	new_tree.root = v

	return new_tree

# This method prints a tree in an order
def PRINT(n,T):
	if n.left_child is None:
		print n,
	else:
		PRINT(T.children[n.left_child],T)
		print n,
		t1 = LEFTMOST_CHILD(n,T)
		t1 = RIGHT_SIBLING(t1,T)
		while t1 is not None:
			PRINT(t1, T)
			t1 = RIGHT_SIBLING(t1, T)
