import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    if isinstance(v, list):
        v = np.array(v)
    if len(np.shape(v)) == 1:
        return np.sqrt(np.dot(v,v))
    else:
        return np.array([
            np.sqrt(np.dot(u,u)) for u in v
        ])