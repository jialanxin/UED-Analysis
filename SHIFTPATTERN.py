import numpy as np
import scipy as sp


def shiftpattern(a, center, center0, flag=0):
    l = np.max(a.shape)
    if flag == 1:
        dct = np.subtract(center, center0)
    else:
        dct = np.subtract(center, center0)
        X = np.arange(dct[1], l+dct[1])
        Y = np.arange(dct[0], l+dct[0])
        mask = sp.interpolate.interp2d(X, Y, a, kind='linear')
        xnew = np.arange(0, l)
        ynew = np.arange(0, l)
        a2 = mask(xnew, ynew)
    return a2
