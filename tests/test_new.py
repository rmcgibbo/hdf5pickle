import os
import numpy as np
from hdf5pickle import dump, load

def test_1():
    try:
        a = np.array(['sdf', {'a': 'b'}])
        dump(a, 'test.hdf5')
        a2 = load('test.hdf5')
        assert a[0] == a2[0]
        assert a[1] == a2[1]
    finally:
        os.unlink('test.hdf5')