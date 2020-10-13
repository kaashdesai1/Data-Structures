# This method evaluates preorder arithmetic expressions
def preorder_calc(T):

	part = ((len(T)+1)/2)
	if len(T) == 3:
		if T[0] == '+':
			return T[1] + T[2]
		elif T[0] == '-':
			return T[1] - T[2]
		elif T[0] == '*':
			return T[1] * T[2]
		elif T[0] == '/':
			return T[1] / T[2]

	else:
		if T[0] == '+':
			return preorder_calc(T[1:part]) + preorder_calc(T[part:])
		elif T[0] == '-':
			return preorder_calc(T[1:part]) - preorder_calc(T[part:])
		elif T[0] == '*':
			return preorder_calc(T[1:part]) * preorder_calc(T[part:])
		elif T[0] == '/':
			return preorder_calc(T[1:part]) / preorder_calc(T[part:])
	return 0 
