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
    

def pca(inputM):
    data = deepcopy(inputM)
    MtM = np.dot(data.T, data)
    evals, evecs = np.linalg.eig(MtM)
    indices = np.argsort(evals)
    indices = indices[::-1]
    evecs = evecs[:,indices]
    evals = evals[indices]
    evecs = evecs.T

    return evecs, evals

    

def pcaCov(inputM, normalise=1, threshold = 0):
    """
    pca  
    """
    data = deepcopy(inputM)
    m = np.mean(data, axis=0)
    data -= m

    data = data.T

    C = np.dot(data.T, data)

    evals, evecs = np.linalg.eig(C)
    indices = np.argsort(evals)
    indices = indices[::-1]
    evecs = evecs[:,indices]
    evals = evals[indices]
    evecs = np.dot(data,evecs)

    if normalise:
        for i in range(np.shape(evecs)[1]):
            evecs[:,i] / np.linalg.norm(evecs[:,i]) * np.sqrt(evals[i])
    evecs = evecs.T

    if threshold:
        total = np.sum(evals)
        s = 0
        i = 0
        while (s/total) < threshold:
                s += evals[i]
                i += 1
        evecs = evecs[:i,:]
        evals = evals[:i]
    return evecs, evals

