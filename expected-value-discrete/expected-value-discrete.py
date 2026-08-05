import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x)
    p = np.array(p)
    if (np.shape(x) != np.shape(p)):
        raise ValueError("Inputs have incompatible shapes.")
    if np.abs(1 - np.sum(p)) >= 10**(-6):
        raise ValueError("Probability distribution is not normalized.")
    return np.dot(x,p)
