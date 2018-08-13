# load data
from READ_RUNS import read_runs
from SHIFTPATTERN import shiftpattern
from skimage import transform
import symmetrize_quadrant
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import time
import pickle
time0 = time.time()
data = read_runs('C:\\Users\\17154\\Documents\\GaTe_UED SLAC_to Lanxin Jia\\UED data_20180322\\Timezero\\scan1\\',
                 '.tif', 0, 0, [], 3*10**4, [i for i in range(1,4)])
time1 = time.time()
print('step1  %s'%(time1-time0))
d = np.mean(data[59:, :, :], axis=0)-np.mean(data[0:17, :, :], axis=0)
d0 = np.mean(data, axis=0)
P = np.array([[379, 470], [550, 350], [499, 646], [666, 527]])
ctc = np.zeros((4, 2))
for i in range(4):
    a = d0[P[i, 0]-30:P[i, 0]+30, P[i, 1]-30:P[i, 1]+30]
    m1 = np.mean(a, axis=0)
    in1 = np.argmax(m1)
    ctc[i, 0] = in1+P[i, 0]-31
    m2 = np.mean(a, axis=1)
    in2 = np.argmax(m2)
    ctc[i, 1] = in2+P[i, 1]-31
ct = np.mean(ctc, axis=0)
centroid = ct
datar = data
angle = 0
ct0 = [513, 513]
for j in range(data.shape[0]):
    datar[j, :, :] = transform.rotate(
        shiftpattern(data[j, :, :], ct, ct0), angle, order=3)
datasym = datar
time2 = time.time()
print('step2  %s'%(time2-time1))
for i in range(130):  #datar.shape[0]
    print(i)
    a = symmetrize_quadrant(datar[i, :, :], 513, 513)
    datasym[i, :, :] = a[601-512-1:601+511, 601-512-1:601+511]


# pickle a variable to a file
file = open('datasave', 'wb')
pickle.dump(datasym, file)
file.close()

# dataf = np.zeros((91, 1024, 1024))
# ref = np.mean(datasym[:17, :, :])
# for z1 in range(1024):
#     for z2 in range(1024):
#         dataf[:, z1, z2] = np.abs(np.fft.fft(datasym[30:121, z1, z2]-np.multiply(
#             np.ones((91, 1, 1)), ref[z1, z2]), axis=0))

# for z in range(6):
#     f = sp.signal.medfilt2d(
#         np.log(np.mean(dataf[z*3-2:z*3, :, :])), kernel_size=10)
#     plt.figure()
#     plt.imshow(f)
#     plt.show()
