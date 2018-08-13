import numpy as np
cimport numpy as np
cimport cython
DTYPE = np.double
ctypedef np.double_t DTYPE_t
TTYPE = np.int64
ctypedef np.int64_t TTYPE_t

def remove_zeros_sub(np.ndarray[DTYPE_t,ndim = 2] Q):
    cdef int sz0 = Q.shape[0]
    cdef int sz1 = Q.shape[1]
    cdef np.ndarray[DTYPE_t,ndim=2] Q2 = Q
    cdef int yy
    cdef int xx
    cdef np.ndarray[DTYPE_t,ndim=2] sub
    for yy in range(1,sz0-1):
        for xx in range(1,sz1-1):
            if Q[yy,xx]==0:
                sub=Q[yy-1:yy+1,xx-1:xx+1]
                f = sub[~np.isnan(sub)].size
                Q2[yy,xx]=np.sum(sub[np.nonzero(sub)])/f
    return Q2
            
def symmetrize_quadrant(np.ndarray[DTYPE_t,ndim=2] a,int ct0, int ct1, int f=1):
    cdef int sz0 = a.shape[0]
    cdef int sz1 = a.shape[1]
    cdef double yl = np.ceil(np.max([ct0, sz0-ct0])/100)*100
    cdef int ylint = int(yl)
    cdef double xl = np.ceil(np.max([ct1, sz1-ct1])/100)*100
    cdef int xlint = int(yl)
    cdef np.ndarray[DTYPE_t,ndim=2] a_s = np.zeros((ylint, xlint))
    cdef int z1
    cdef int z2
    cdef double m
    cdef int n
    for z1 in range(ylint):
        for z2 in range(xlint):
            m = 0
            n = 0
            if ct0+z1 <= sz0 and ct1+z2 <= sz1:
                if ~np.isnan(a[ct0+z1-1, ct1+z2-1]) :
                    m = m+a[ct0+z1-1, ct1+z2-1]
                    n = n+1
            if ct0+z1 <= sz0 and ct1-z2 >= 1:
                if ~np.isnan(a[ct0+z1-1, ct1-z2-1]):
                    m = m+a[ct0+z1-1, ct1-z2-1]
                    n = n+1
            if ct0-z1>=1 and ct1+z2<=sz1:
                if ~np.isnan(a[ct0-z1-1,ct1+z2-1]):
                    m=m+a[ct0-z1-1,ct1+z2-1]
                    n = n+1
            if ct0-z1>=1 and ct1-z2>=1:
                if ~np.isnan(a[ct0-z1-1,ct1-z2-1]):
                    m=m+a[ct0-z1-1,ct1-z2-1]
                    n=n+1
            if n == 0:
                a_s[z1,z2]=0
            else:
                a_s[z1,z2]=m/n
    a = a_s
    sz0 = a.shape[0]
    sz1 = a.shape[1]
    a_s  = np.zeros((2*ylint,2*xlint))
    ct0 = ylint
    ct1 = xlint
    for z1 in range(sz0-1):
        for z2 in range(sz1-1):
            a_s[ct0+z1,ct1+z2]=a[z1,z2]
            a_s[ct0+z1,ct1-z2]=a[z1,z2]
            a_s[ct0-z1,ct1+z2]=a[z1,z2]
            a_s[ct0-z1,ct1-z2]=a[z1,z2]
    a_s = remove_zeros_sub(a_s)
    return a_s
