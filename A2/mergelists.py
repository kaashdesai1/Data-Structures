import arraylist


# This method is used to merge sorted lists
def merge_array(List_1, List_2):
	result = []
	result = arraylist.MAKENULL(result)
	p1 = 0
	p2 = 0
	total = len(List_1) + len(List_2)
	
	while len(result) != total:
		if len(List_1) == p1:
			for i in range(p2, len(List_2)):
				arraylist.INSERT(List_2[i],(len(result)-1), result)
			break
		elif len(List_2) == p2:
			for j in range(p1,len(List_1)):
				arraylist.INSERT(L1[j],(len(result),-1), result)
			break
		elif List_1[p1] < List_2[p2]:
			arraylist.INSERT(List_1[p1], (len(result)-1), result)
			p1 += 1
		else:
			arraylist.INSERT(List_2[p2], (len(result)-1), result)
			p2 += 1
	return result


# This method is used to break down mulitple lists for merging
def merge_m(l):
	if len(l) == 0:
		return
	elif len(l) == 1:
		return l[0]
	else:
		t1 = merge_array(l[0], l[1])
		for i in range(2,len(l)):
			t1 = merge_array(t1, l[i])
		return t1

def main():
	List_1 = []; List_2 = []; List_3 = []; List_4 = [] 

	for i in xrange(11,1,-1):
		arraylist.INSERT(i,0, List_1)
	
	for j in xrange(22,2,-2):
		arraylist.INSERT(j,0, List_2)

	for k in xrange(33,3,-3):
		arraylist.INSERT(k,0, List_3)

	for y in xrange(44,4,-4):
		arraylist.INSERT(y,0, List_4)
	
	# Printing each individual list
	print "List 1: ", arraylist.PRINT(List_1)
	print "List 2: ", arraylist.PRINT(List_2)
	print "List 3: ", arraylist.PRINT(List_3)
	print "List 4: ", arraylist.PRINT(List_4)

	# print merge of all four list
	l = [List_1, List_2, List_3, List_4]

	merged_list = merge_m(l)
	print "Merging ALL:", merged_list	

main()
