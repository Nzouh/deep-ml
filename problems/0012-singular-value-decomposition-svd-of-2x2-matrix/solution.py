import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    # Must first calculate for A^T * A
    gram_matrix = A.T @ A

    #next, we find the sigma matrix

    # A = U SIGMA V^T
    # AV = U SIGMA V^T V
    # AV = U SIGMA

    #find the eigenvalues

    #so we have to do det( G - lambdaI)

    grama = gram_matrix[0][0]
    gramb = gram_matrix[0][1]
    gramd = gram_matrix[1][1]


    #Find the angle theta

    theta = 0.5 * np.arctan2(2 * gramb, grama - gramd)
    c = np.cos(theta)
    s = np.sin(theta)

    V = np.array([[c, -s], [s, c]])

    #find V^T G V:

    D = V.T @ gram_matrix @ V

    #find all the diagonal entries

    singular_value1 = np.sqrt(max(D[0][0], 0))
    singular_value2 = np.sqrt(max(D[1][1], 0))

    S = np.array([singular_value1, singular_value2])

    #We know that AV = U S

    #Thus , U = A * v * S ^ -1

    U = (A @ V) / S

    return U, S, V.T