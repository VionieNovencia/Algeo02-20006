import numpy as np
from numpy.linalg import qr


def eigenvalue(x):
    eigen = []
    a = x
    for i in range(1000):
        q, r = qr(a)
        a = np.dot(r, q)
    for j in range(a.shape[0]):
        eigen.append(np.round(a[j][j],12))

    return np.unique(eigen)