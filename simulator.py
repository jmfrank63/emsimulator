# A simple field simulator for charged particles

import numpy as np
from scipy.spatial.distance import euclidean

def vector(start,end):
    '''
    Takes a list of tuples
    '''
    return np.subtract(np.array(end), np.array(start))


print(vector((0,-1,0),(1,1,1))*.5)
print((1,1,1)/np.linalg.norm((1,1,1)))
