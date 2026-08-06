import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # check for non-square input
    (H,W) = np.shape(A)
    if (H != W):
        return None
    # check for non-invertibility via determinant
    if np.abs(np.linalg.det(A)) < 10**(-6):
        return None
    # otherwise, just invert
    return np.linalg.inv(A)
