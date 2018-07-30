import matplotlib.image as mpimg
import numpy as np
def read_tif(Pathname, Filename, highvalue=6*10**4):
    if Pathname[-1] != '\\':
        Pathname = Pathname + '\\'
    if Filename[-4:-1] != '.tif':
        Filename = Filename + '.tif'
    a = mpimg.imread(Pathname+Filename)
    height, width = a.shape
    if height*width = 1024**2:
        asub = a[0:99,0:99]
    else:
        asub = a[-1,:]
    a = a - np.median(asub)
    a[a>highvalue] = np.nan