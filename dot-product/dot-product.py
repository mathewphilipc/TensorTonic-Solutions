import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Assume x,y are either both lists or both np.arrays, numeric
    # types only, no nesting, not necessarily compatible lengths.
    if isinstance(x, list):
        if (len(x) != len(y)):
            raise ValueError("Mismatched lengths")
        L = len(x)
        return float(sum(x[i]*y[i] for i in range(L)))
    else:
        if (np.shape(x) != np.shape(y)):
            raise ValueError("Mismatched shapes")
        return np.dot(x,y)