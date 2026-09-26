def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	
	for i in range(len(matrix)):
		result = [item * scalar for item in matrix[i]]
		matrix[i] = result

	return matrix
