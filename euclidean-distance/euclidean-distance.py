import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Assume x, y are either both lists or both np arrays.
    # Assume numeric entries, no nesting, not necessarily compatible shapes.
    if (isinstance(x, list)):
        if (len(x) != len(y)):
            raise ValueError('Incompatible shapes.')
        L = len(x)
        return np.sqrt(sum((x[i] - y[i])**2 for i in range(L)))
    else:
        if (np.shape(x) != np.shape(y)):
            raise ValueError('Incompatible shapes')
        return np.sqrt(np.dot(x - y, x - y))