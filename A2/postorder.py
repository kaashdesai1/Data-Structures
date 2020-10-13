# This method evaluates postorder arithmetic expressions
def postorder_calc(T):
	top = len(T) - 1
	part = ((len(T)-1)/2)

	if len(T) == 3:
		if T[top] == '+':
			return T[0] + T[1]
		elif T[top] == '-':
			return T[0] - T[1]
		elif T[top] == '*':
			return T[0] * T[1]
		elif T[top] == '/':
			return T[0] / T[1]
	else:
		if T[top] == '+':
			return postorder_calc(T[:part]) + postorder_calc(T[part:top])
		elif T[top] == '-':
			return postorder_calc(T[:part]) - postorder_calc(T[part:top]) 
		elif T[top] == '*':
			return postorder_calc(T[:part]) * postorder_calc(T[part:top]) 
		elif T[top] == '/': 
			return postorder_calc(T[:part]) / postorder_calc(T[part:top]) 
	return 0
