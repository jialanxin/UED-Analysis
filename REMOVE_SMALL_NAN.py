import numpy as np
from skimage import morphology
from numba import jit


def remove_small_nan(Image, objsize=50, flag=1, Length=20):
    f1 = np.isnan(Image)
    f2 = morphology.remove_small_objects(f1, objsize)
    f = f1.astype(int) - f2.astype(int)
    Removedimage = Image
    Y, X = np.nonzero(f)
    rd = np.rint(Length/2)
    lth = np.maximum(Image.shape[0], Image.shape[1])
    for z in range(Y.size):
        ymin = np.maximum(Y[z]-rd, 1).astype(int)-1
        ymax = np.minimum(Y[z]+rd, lth).astype(int)-1
        xmin = np.maximum(X[z]-rd, 1).astype(int)-1
        xmax = np.minimum(X[z]+rd, lth).astype(int)-1
        region = Image[ymin:ymax, xmin:xmax]
        if flag == 0:
            region = region.view()
            region = region[~np.isnan(region)]
            sumary = np.sum(region)
            region = region[np.nonzero(region)]
            nnz = region.size
            value = sumary/nnz
        elif flag == 1:
            region = region.view()
            region = region[~np.isnan(region)]
            value = np.median(region)
        Removedimage[Y[z], X[z]] = value
    return Removedimage
