import pointerqueue
import lcrstree


# This method implements a level order (n - node, T - tree, Q - queue, p - position)
def level_order(n, T, Q, p):

	if lcrstree.LEFTMOST_CHILD(n, T) is None:
		if Q[p] is None:
			Q[p] = pointerqueue.pointer_queue()
		pointerqueue.ENQUEUE(n.label, Q[p])
		return
	else:
		temp = lcrstree.LEFTMOST_CHILD(n, T)
		while temp is not None:
			level_order(temp, T, Q, p+1)
			temp = lcrstree.RIGHT_SIBLING(temp, T)
			if Q[p] is None:
				Q[p] = pointerqueue.pointer_queue()
		pointerqueue.ENQUEUE(n.label, Q[p])

def main():
	Tree_1 = lcrstree.CREATE0(4); Tree_2 = lcrstree.CREATE0(5); Tree_3 = lcrstree.CREATE2(2,Tree_1,Tree_2);
	Tree_6 = lcrstree.CREATE0(6); Tree_7 = lcrstree.CREATE0(7); Tree_4 = lcrstree.CREATE2(3, Tree_6, Tree_7)
 	T = lcrstree.CREATE2(1, Tree_3, Tree_4)
	
	print "\nInorder Printing of Tree: ",
	lcrstree.PRINT(lcrstree.ROOT(T), T)	
	
	print "Level-order print: "
	
	t1 = [None]*100

	level_order(lcrstree.ROOT(T), T, t1, 0)

	for i in range(0,len(t1)) :
		if t1[i] is not None :
			print "Level",i,':\n',
			pointerqueue.PRINT(t1[i])

main()
