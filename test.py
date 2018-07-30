import matplotlib.image as mpimg
import numpy as np
# a = mpimg.imread(r'C:\Users\17154\Documents\GaTe_UED SLAC_to Lanxin Jia\UED data_20180322\D3\scan7\run001\images-ANDOR1\ANDOR1_delayHigh-004--08.8000_0001.tif')
# asub = a[0:99,0:99]
y =np.array([ [1,0,np.nan],[2,0,np.nan]])
y = y.view()
y = y[~np.isnan(y)]
print(len(y))