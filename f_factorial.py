def computeFactorial(num):
	# docstring example
	# for help on docstring: "help f_facorial.py"
	""" Returns factorial result.
	    Returns factorial computed 1 to <num> for parameter <num>."""
	int_result = 1
	x = 1
	for x in range(x, num + 1):
		int_result = x * int_result 
	return int_result