import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Extract shape of A, exposed by np as tuple.
    (H, W) = np.shape(A)

    # Create new array of transposes shape.
    B = np.zeros((W,H))

    # Populate and return B.
    for i in range(H):
        for j in range (W):
            B[j][i] = A[i][j]
    return B