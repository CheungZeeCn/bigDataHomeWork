""" Principal Component Analysis.
Implemented by two methods for finding priciples.
God blesses me

                        cheungzeecn@gmail.com
"""
from copy import deepcopy
import numpy as np

def pcaSvd(inputM):
    data = deepcopy(inputM)
    print data.shape 
    s, sigma, vt = np.linalg.svd(data)
    return vt, sigma
    
