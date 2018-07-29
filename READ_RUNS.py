from READ_SCAN import read_scan


def read_runs(parrentfloder, filestem, hotpixel, flag, AG, highvalue, runrange, datacol=[], posi=[]):
    z1 = runrange[0]
    z2 = runrange[-1]
    timestamp = []
    for z in range(z1, z2):
        folderpath = '{}\\run00{}\images-ANDOR1\\'.format(parrentfloder,z)
        [datacol1 , posi1, timestamp1] = read_scan(folderpath, filestem, hotpixel, flag ,AG , highvalue)
