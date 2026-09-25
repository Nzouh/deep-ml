def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    new_lst= []
    for column in range(len(a[0])):
        new_lst.append([])
        for row in range(len(a)):
            new_lst[column].append(a[row][column])
    
    return new_lst


        

    pass