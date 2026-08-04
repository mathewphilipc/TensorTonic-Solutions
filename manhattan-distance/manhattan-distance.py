import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """

    # Assume x, y both lists or both numpy arrays, neither nested, same length
    if isinstance(x, list):
        L = len(x)
        return float(sum(np.abs(x[i] - y[i]) for i in range(L)))
    else:
        return float(np.sum(np.abs(x - y)))