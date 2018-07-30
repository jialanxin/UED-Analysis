import numpy as np
import os
def read_scan(folderpath, filestem='.tif', hotpixel=0, flag=1, AG=np.ones(1,1024,1024), highvalue=70000):
    listing = os.listdir(folderpath)
    n = []
    timestamp = []
    posi0=[]
    for i in listing:
        if os.path.splitext(i)[1] == filestem:
            n.append(i)
    a = 
