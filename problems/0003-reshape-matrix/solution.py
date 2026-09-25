import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
		return []
	
	flat_lst = [element for row in a for element in row]
	
	reshaped_matrix = [flat_lst[i:i + new_shape[1]] for i in range(0, len(flat_lst), new_shape[1])]

	return reshaped_matrix