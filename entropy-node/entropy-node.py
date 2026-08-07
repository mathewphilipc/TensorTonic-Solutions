import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    if len(y) == 0:
        return 0.0
    freq_dict = {}
    for entry in y:
        if not (entry in freq_dict):
            freq_dict[entry] = 0
        freq_dict[entry] += 1

    freqs = np.array(list(freq_dict.values()))
    probs = freqs / np.sum(freqs)
    entropy = - sum(p*np.log2(p) for p in probs)
    return entropy
        