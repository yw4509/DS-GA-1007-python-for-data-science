import sys
import numpy as np
import scipy.sparse

def getsizeof(input):
    # return the memory footprint 
    if isinstance(input, np.ndarray):
        return input.nbytes
    elif isinstance(input, scipy.sparse.csr.csr_matrix):
        return input.data.nbytes + input.indices.nbytes + input.indptr.nbytes 
    else:
        return sys.getsizeof(input)