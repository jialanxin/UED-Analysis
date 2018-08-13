import numpy as np
import pickle
import scipy.signal as sp
import matplotlib.pyplot as plt
with open('datasave', 'rb') as file:
    datasym =pickle.load(file)
dataf = np.zeros((91, 1024, 1024))
ref = np.mean(datasym[:17, :, :],axis=0)
for z1 in range(1024):
    for z2 in range(1024):
        value1 =datasym[30:121, z1, z2]
        value2 = np.multiply(np.ones((91,)),ref[z1, z2])
        dataf[:, z1, z2] = np.abs(np.fft.fft(value1-value2, axis=0))

for z in range(6):
    f = sp.medfilt2d(
        np.log(np.mean(dataf[z*3-2:z*3, :, :],axis=0)), kernel_size=11)
    plt.figure()
    plt.imshow(f)
    plt.show()
