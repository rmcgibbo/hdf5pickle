import os
import numpy as np
import joblib
import hdf5pickle
import time
from six.moves import cPickle

model = {'unicode string': u'unicode string',
         'bytes string': b'bytes string',
         'array': np.around(np.sin(np.arange(100000)), 4)}


def printline(package, compress, writetime, readtime, size):
    print('%10s\t%10s\t%.3f\t\t%.3f\t\t%s' % (package, compress, writetime, readtime, size))
print('%10s\tCompression\tWrite Time\tRead Time\tSize' % ('Package'))

for compress in [0,1,3,9]:
    for package in [joblib, hdf5pickle]:
        start = time.time()
        package.dump(model, 'path', compress=compress)
        end = time.time()

        writetime = end-start

        start = time.time()
        package.load('path')
        end = time.time()
        readtime = end-start

        printline(package.__name__, compress, writetime, readtime, os.stat('path').st_size)

start = time.time()
with open('path', 'wb') as f:
    cPickle.dump(model, f)
end = time.time()
writetime = end-start

start = time.time()
with open('path', 'rb') as f:
    cPickle.load(f)
end = time.time()
readtime = end-start

printline('pickle', 'N/A', writetime, readtime, os.stat('path').st_size)
