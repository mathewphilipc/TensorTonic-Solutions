import numpy as np

# check if input is a numeric-type scalar
# could be more thorough with type-checking, but this is probably
# fine enough for tests here
def isnum(x):
    return (isinstance(x, float) or isinstance(x, int))

# pass numeric-type scalar through sigmoid function
def scalarsigmoid(x):
    return 1 / (1 + np.exp(-x))
    

# recursively apply sigmoid element-wise to (generally nested) list
# with numeric types at the bottom
def listsigmoid(x):
    if isnum(x):
            return scalarsigmoid(x)
    return [listsigmoid(elem) for elem in x]

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    if isinstance(x, np.ndarray):
        return 1/(1 + np.exp(-x))
    elif isnum(x):
        return scalarsigmoid(x)
    elif isinstance(x, list):
        return np.array(listsigmoid(x))
    else:
        return None
    return x