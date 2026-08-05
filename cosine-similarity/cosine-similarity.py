import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    adota = np.dot(a,a)
    bdotb = np.dot(b,b)
    if (adota == 0 or bdotb == 0):
        return 0
    return np.dot(a,b) / np.sqrt(adota*bdotb)