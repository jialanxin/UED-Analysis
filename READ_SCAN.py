import numpy as np
import os
from READ_TIF import read_tif
from REMOVE_SMALL_NAN import remove_small_nan
import numpy as np
import scipy as sp
from numba import jit


def read_scan(folderpath, filestem='.tif', hotpixel=0, flag=1, AG=np.ones((1024, 1024)), highvalue=70000):
    listing = os.listdir(folderpath)
    n = []
    posi0 = []
    for i in listing:
        if os.path.splitext(i)[1] == filestem:
            n.append(i)
            st = i.find('.tif')
            posi0.append(float(i[st-12:st-6]))
    a = read_tif(folderpath, n[-1], highvalue)
    sz = a.shape
    posi, ic = np.unique(posi0, return_inverse=True)
    if flag == 0:
        Nor = np.zeros((posi.size, sz[0], sz[1]))
        datacol = np.zeros((posi.size, sz[0], sz[1]))
        for z in range(ic.size):
            A = read_tif(folderpath, n[z], highvalue)
            if np.isnan(np.sum(AG)) == True:
                NAG = np.sum(np.isnan(AG))
                Image = np.multiply(A, AG)
                A = remove_small_nan(
                    Image, NAG+100, 1, np.ceil(np.sqrt(NAG)+5))
            if hotpixel == 1:
                A = sp.signal.medfilt2d(A, 15)
            datacol[ic[z], :, :] = datacol[ic[z], :, :] + \
                A.reshape((1, sz[0], sz[1]))
            Nor[ic[z], :, :] = Nor[ic[z], :, :]+np.ones((1, sz[0], sz[1]))
        datacol = np.divide(datacol, Nor)
    elif flag == 1:
        dn = []
        datacol = np.zeros(np.array(posi0).size, sz[0], sz[1])
        for j in n:
            A = read_tif(folderpath, j, highvalue)
            path = os.path.join(folderpath, j)
            tm = os.path.getmtime(path)
            dn.append(tm)
            if np.isnan(np.sum(AG)) == True:
                NAG = np.sum(np.isnan(AG))
                Image = np.multiply(A, AG)
                A = remove_small_nan(
                    Image, NAG+100, 1, np.ceil(np.sqrt(NAG)+5))
            if hotpixel == 1:
                A = sp.signal.medfilt2d(A, 15)
            datacol[j, :, :] = datacol[j, :, :] + A.reshape((1, sz[0], sz[1]))
        ind = np.argsort(dn)
        posi = posi0[ind]
        datacol = datacol[ind, :, :]
    return datacol, posi
