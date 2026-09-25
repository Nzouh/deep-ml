def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	if mode == "column":
		return [sum(matrix[i][j] for i in range(len(matrix))) / (len(matrix)) for j in range(len(matrix[0]))]

	elif mode == "row":
		return [sum(j for j in i) / len(matrix[0]) for i in matrix]
	
	else:
		raise ValueError("Incorrect Value")
	return means