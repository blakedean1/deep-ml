import numpy as np

def calculate_dot_product(vec1, vec2):
	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The dot product of the two vectors.
	"""
	# Your code here
	sum_list = []
	total = 0
	for i in range(len(vec1)):
		sum_list.append(vec1[i] * vec2[i])

	for i in sum_list:
		total += i

	return total