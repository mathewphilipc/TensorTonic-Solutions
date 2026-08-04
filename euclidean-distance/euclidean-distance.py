import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Assume x, y are either both lists or both np arrays.
    # Assume numeric entries, no nesting, not necessarily compatible shapes.
    if (isinstance(x, list)):
        x = np.array(x)
    if (isinstance(y, list)):
        y = np.array(y)
    if (np.shape(x) != np.shape(y)):
        raise ValueError('Incompatible shapes')
    return np.sqrt(np.dot(x - y, x - y))