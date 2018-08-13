import scipy.signal as sp
import numpy as np
a = np.arange(100).reshape((10,10))
b = sp.medfilt2d(a)
print(b)