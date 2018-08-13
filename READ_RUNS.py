from READ_SCAN import read_scan
import numpy as np


def read_runs(parrentfloder, filestem, hotpixel, flag, AG, highvalue, runrange, datacol=[], posi=[]):
    z1 = runrange[0]
    z2 = runrange[-1]+1
    for z in range(z1, z2):
        folderpath = '{}\\run00{}\\images-ANDOR1\\'.format(parrentfloder, z)
        datacol1, posi1 = read_scan(
            folderpath, filestem, hotpixel, flag, AG, highvalue)
        datacol1 = np.array(datacol1)
        datacol = np.append(datacol,datacol1)
        posi = np.append(posi,posi1)
        datacol = datacol.reshape((-1, 1024, 1024))
    return datacol
