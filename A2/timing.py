from timeit import timeit, Timer

import loctree
import lcrstree


def pr_loctree_test():
	print
	def create_loctree(v,n):
		if n == 0:
			return loctree.CREATE0(v)
		else:
			return loctree.CREATE3(v, create_loctree((3*n)-1,n-1), create_loctree((3*n),n-1),create_loctree((3*n)+1,n-1))

	def preorder_traverse_loctree(n,T):
		if loctree.LEFTMOST_CHILD(n,T) is None:
			return
		else:
			preorder_traverse_loctree(loctree.LEFTMOST_CHILD(n,T),T)
			t1 = loctree.LEFTMOST_CHILD(n,T)
			t1 = loctree.RIGHT_SIBLING(t1,T)
			while t1 is not None:
				preorder_traverse_loctree(t1,T)
				t1 = loctree.RIGHT_SIBLING(t1,T)

	test = loctree.tree()
	print "########## LOC Tree Preorder Traversal ##########"
	print "Size", "Time (ms)"
	for size in xrange(1,5,1):
		test = create_loctree(1,size)
		def loctree_trav():
			preorder_traverse_loctree(loctree.ROOT(test),test)
		time = Timer(loctree_trav)
		travtime = time.timeit(1)
		print size,"  ", travtime*1000
	print


def pr_lcrstree_test():
	print
	def create_lcrstree(v,n):
		if n == 0:
			return lcrstree.CREATE0(v)
		else:
			return lcrstree.CREATE3(v, create_lcrstree((3*n)-1,n-1), create_lcrstree((3*n),n-1),create_lcrstree((3*n)+1,n-1))
	def preorder_traverse_lcrstree(n,T):
		if lcrstree.LEFTMOST_CHILD(n,T) is None:
			return
		else:
			preorder_traverse_lcrstree(lcrstree.LEFTMOST_CHILD(n,T),T)
			t1 = lcrstree.LEFTMOST_CHILD(n,T)
			t1 = lcrstree.RIGHT_SIBLING(t1,T)
			while t1 is not None:
				preorder_traverse_lcrstree(t1,T)
				t1 = lcrstree.RIGHT_SIBLING(t1,T)

	test = lcrstree.tree()
	print "########## LCRS Tree Preorder Traversal ##########"
	print "Size", "Time (ms)"
	for size in xrange(1,5,1):
		test = create_lcrstree(1,size)
		def lcrstree_trav():
			preorder_traverse_lcrstree(lcrstree.ROOT(test),test)
		time = Timer(lcrstree_trav)
		travtime = time.timeit(1)
		print size, "  ", travtime*1000
	print

pr_loctree_test()
pr_lcrstree_test()
