import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	

	trace = matrix[0][0] + matrix[1][1]
	determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

	eigenvalue1 = (trace + math.sqrt(trace ** 2 - (4 * determinant))) / (2) 
	eigenvalue2 = (trace - math.sqrt(trace ** 2 - 4 * determinant)) / (2) 


	return [eigenvalue1, eigenvalue2]