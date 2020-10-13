import arraylist

# This method is sued to concatenate a list

def list_concat(List_1, List_2):
	result = []
	result = arraylist.MAKENULL(result)
	p1 = 0
	p2 = 0
	total = len(List_1) + len(List_2)
	for i in range(0, len(List_1)):
		arraylist.INSERT(List_1[i],(len(result)-1),result)

	for j in range(0, len(List_2)):
		arraylist.INSERT(List_2[j],(len(result)-1), result)
	return result


# break down list of list
def concat_m(l):
	if len(l) == 0:
		return
	elif len(l) == 1:
		return l[0]
	else:
		t1 = list_concat(l[0], l[1])
		for i in range(2,len(l)):
			t1 = list_concat(t1, l[i])
		return t1

def main():
	
	List_1 = []; List_2 = []; List_3 = []; List_4 = [] 

	for i in xrange(11, 1, -1):
		arraylist.INSERT(i, 0, List_1)
	
	for j in xrange(22, 2, -2):
		arraylist.INSERT(j, 0, List_2)

	for k in xrange(33, 3,-3):
		arraylist.INSERT(k, 0, List_3)

	for y in xrange(44, 4, -4):
		arraylist.INSERT(y, 0, List_4)
	
	# print individual list
	print "L1: ", arraylist.PRINT(List_1)
	print "L2: ", arraylist.PRINT(List_2)
	print "L3: ", arraylist.PRINT(List_3)
	print "L4: ", arraylist.PRINT(List_4)

	# print merge of all four list
	l = [List_1, List_2, List_3, List_4]

	concated_list = concat_m(l)
	print "Concatenate ALL: ", concated_list
		
main()
