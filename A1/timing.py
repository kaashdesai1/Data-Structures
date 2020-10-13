from timeit import timeit, Timer

import arraylist
import arraystack
import pointerlist
import pointerstack

class Stack:
	def __init__(self):
  		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

  	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[len(self.items)-1]
	
	def size(self):
		return len(self.items)	


def print_time(x):

	time = Timer(x)
	print time.timeit(1)*1000, 'ms'


def list_test():

	print "******************************************\n"
	print "************** LIST TESTING **************\n"
	print "******************************************\n\n"


	print "----------ITERATED INSERTION----------\n"
	print "1. Forward Testing"

	for ADT_size in xrange(1000, 3000, 500):
		print "\nData Structure Size (# of elements): ", ADT_size
		
		def f_built_in():
			l = []

			for i in xrange(0, ADT_size):
				l.insert(0, i)

		print_time(f_built_in)

		def f_array_implement():
			array_implement = []
			array_implement = arraylist.MAKENULL(array_implement)
			for i in xrange(0, ADT_size):
				arraylist.INSERT(i, 0, array_implement)
		
		print_time(f_array_implement)

		def f_pointer_implement():
			pointer_implement = pointerlist.pointer_list()
			for i in xrange(0, ADT_size):
				pointerlist.INSERT(i, 0, pointer_implement)
		
		print_time(f_pointer_implement)

	f_built_in()
	f_array_implement()
	f_pointer_implement()

	print "\n2. Backward Testing"

	for ADT_size in xrange(1000, 3000, 500):
		print "\nData Structure Size (# of elements): ", ADT_size
		
		def b_built_in():
	 		l = []
			reverse = ADT_size

			for i in xrange(0, ADT_size):
				l.append(i)

		print_time(b_built_in)

		def b_array_implement():
			array_implement = []
			reverse = ADT_size
			array_implement = arraylist.MAKENULL(array_implement)
			for i in xrange(0, ADT_size):
				arraylist.INSERT(i,reverse,array_implement)
				reverse = reverse - 1
		
		print_time(b_array_implement)


		def b_pointer_implement():
			pointer_implement = pointerlist.pointer_list()
			reverse = ADT_size - 1
			for i in xrange(0, ADT_size):
				pointerlist.INSERT(i, reverse, pointer_implement)
				reverse = reverse - 1
		
		print_time(b_pointer_implement)

	b_built_in()
	b_array_implement()
	b_pointer_implement()

	print "\n----------TRAVERSAL----------\n"

	for ADT_size in xrange(1000, 3000, 500):
		
		print "\nData Structure Size (# of elements): ", ADT_size
		l = []
		for i in xrange(0, ADT_size):
			l.insert(0, i)
		
		def traverse_built_in():
			for num in xrange(0, len(l)):
				t = l[i]
		
		print_time(traverse_built_in)


		array_implement = []
		array_implement = arraylist.MAKENULL(array_implement)
		
		for i in xrange(0, ADT_size):
			arraylist.INSERT(i, 0, array_implement)
		
		def traverse_array_implement():
			for num in xrange(0, len(array_implement)):
				t = arraylist.RETRIEVE(num, array_implement)

		print_time(traverse_array_implement)


		pointer_implement = pointerlist.pointer_list()
		for i in xrange(0,ADT_size):
			pointerlist.INSERT(i, 0, pointer_implement)

		def traverse_pointer_implement():
			p = 0
			t1 = pointerlist.FIRST(pointer_implement)
			while t1:
				t = pointerlist.RETRIEVE(p,pointer_implement)
				p = p + 1
				t1 = t1.nxt
		
		print_time(traverse_pointer_implement)

	traverse_built_in()
	traverse_array_implement()
	traverse_pointer_implement()


	print "\n----------ITERATED DELETION----------\n"

	print "1. Forward Testing"

	for ADT_size in xrange(1000, 3000, 500):
		print "\nData Structure Size (# of elements): ", ADT_size
		
		l = []
		for i in xrange(0, ADT_size):
			l.insert(0, i)

		def df_built_in():
			end = len(l) - 1
			for element in l:
				l.remove(element)

		print_time(df_built_in)


		array_implement = []
		array_imp = arraylist.MAKENULL(array_implement)
		for i in xrange(0, ADT_size):
			arraylist.INSERT(i, 0, array_implement)
		
		def df_array_implement():
			for p in xrange(0,len(array_implement)):
				arraylist.DELETE(p,array_implement)

		print_time(df_array_implement)


		pointer_implement = pointerlist.pointer_list()
		for i in xrange(0, ADT_size):
			pointerlist.INSERT(i, 0, pointer_implement)

		def df_pointer_implement():
			p = 0
			t1 = pointer_implement.head

			while t1:
				pointerlist.DELETE(p, pointer_implement)
				t1 = t1.nxt
				p = p + 1

		print_time(df_pointer_implement)

	df_built_in()
	df_array_implement()
	df_pointer_implement()


	print "\n2. Backward Testing"

	for ADT_size in xrange(1000, 3000, 500):
		print "\nData Structure Size (# of elements): ", ADT_size
		l = []
		for i in xrange(0, ADT_size):
			l.insert(0, i)
		
		def db_built_in():
			last = len(l) - 1
			while(last > 0):
				del l[last]
				last = last - 1

		print_time(db_built_in)

		array_implement = []
		array_imp = arraylist.MAKENULL(array_implement)
		
		for i in xrange(0, ADT_size):
			arraylist.INSERT(i, 0, array_imp)
		
		def db_array_implement():
			last = len(array_implement) - 1
			while( last > 0 ):
				arraylist.DELETE(last, array_implement)
				last = last - 1

		print_time(db_array_implement)


		pointer_implement = pointerlist.pointer_list()
		for i in xrange(0, ADT_size):
			pointerlist.INSERT(i, 0, pointer_implement)

		def db_pointer_implement():
			last = ADT_size-1
			t1 = pointer_implement.head
			while t1:
				pointerlist.DELETE(last, pointer_implement)
				last = last - 1
				t1 = t1.nxt

		print_time(db_pointer_implement)

	db_built_in()
	db_array_implement()
	db_pointer_implement()


def stack_test():
	
	print "\n******************************************\n"
	print "************** STACK TESTING **************\n"
	print "******************************************\n\n"

	print "1. Iterated insertion - PUSH operation"

	for ADT_size in xrange(1000, 3000, 500):
		print "\nData Structure Size (# of elements): ", ADT_size
		
		def si_built_in():
			s = Stack()
			for i in xrange(0, ADT_size):
				s.push(i)

		print_time(si_built_in)

		def si_array_implement():
			array_implement = []
			array_implement = arraystack.MAKENULL(array_implement)

			for i in xrange(0,ADT_size):
				array_implement = arraystack.PUSH(i,array_implement)

		print_time(si_array_implement)


		def si_pointer_implement():
			pointer_implement = pointerstack.pointer_stack()

			for i in xrange(0,ADT_size):
				pointerstack.PUSH(i,pointer_implement)

		print_time(si_pointer_implement)


	si_built_in()
	si_array_implement()
	si_pointer_implement()


	print "\n2. Iterated Deletion - POP operation"

	for ADT_size in xrange(1000, 3000, 500):
		print "\nData Structure Size (# of elements): ", ADT_size
	
		s = Stack()
		for i in xrange(0, ADT_size):
			s.push(i)
		
		def sd_built_in():
			for i in xrange(0,ADT_size):
				if s.isEmpty() == False:
					s.pop()

		print_time(sd_built_in)


		array_implement = []
		arraystack.MAKENULL(array_implement)

		for i in xrange(0,ADT_size):
			array_implement = arraystack.PUSH(i, array_implement)
		
		def sd_array_implement():
			for i in xrange(0, ADT_size):
				if arraystack.EMPTY(array_implement) == False:
					arraystack.POP(array_implement)

		print_time(sd_array_implement)

		pointer_implement = pointerstack.pointer_stack()
		for i in xrange(0,ADT_size):
			pointerstack.PUSH(i,pointer_implement)

		def sd_pointer_implement():
			for i in xrange(0,ADT_size):
				if pointerstack.EMPTY(pointer_implement) == False:
					pointerstack.POP(pointer_implement)
		
		print_time(sd_pointer_implement)

	sd_built_in()
	sd_array_implement()
	sd_pointer_implement()


list_test()
stack_test()
