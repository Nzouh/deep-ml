def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	if mode == "column":
		return [sum(column) / len(column) for column in zip(*matrix)]

	elif mode == "row":
		return [sum(i) / len(matrix[0]) for i in matrix]
	
	else:
		raise ValueError("Incorrect Value")