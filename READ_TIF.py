import matplotlib.image as mpimg
import numpy as np
from REMOVE_SMALL_NAN import remove_small_nan
from numba import jit


def read_tif(Pathname, Filename, highvalue=6*10**4):
    if Pathname[-1] != '\\':
        Pathname = Pathname + '\\'
    # if Filename[-4:-1] != '.tif':
    #     Filename = Filename + '.tif'
    a = mpimg.imread(Pathname+Filename)
    height, width = a.shape
    if height*width == 1024**2:
        asub = a[0:99, 0:99]
    else:
        asub = a[-1, :]
    a = a - np.median(asub)
    a[a > highvalue] = np.nan
    I = remove_small_nan(a, a[np.isnan(a)].size+10, 1,
                         np.maximum(np.ceil(np.sqrt(a[np.isnan(a)].size))+1, 50))
    return I
