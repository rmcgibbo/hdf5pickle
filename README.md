hdf5pickle
==========

Fast persistence of Python objects to HDF5 files.

[![Build Status](https://travis-ci.org/rmcgibbo/hdf5pickle.png?branch=master)](https://travis-ci.org/rmcgibbo/hdf5pickle)
[![PyPI Version](https://badge.fury.io/py/hdf5pickle.png)](https://pypi.python.org/pypi/hdf5pickle)
[![Downloads](https://pypip.in/d/hdf5pickle/badge.png)](https://pypi.python.org/pypi/hdf5pickle)

```
>>> import numpy as np
>>> import hdf5pickle

>>> class A(object):
...    def __init__(self):
...        self.x = 100.0
...        self.y = np.ones((1000000))
...        self.z = [{'a': None}, A]
...
...    def __str__(self):
...        return 'x=%s, y=%s, z=%s' % (self.x, self.y, self.z)

>>> hdf5pickle.dump(A(), 'a.hdf5')
>>> print(hdf5pickle.load('a.hdf5'))
x=100.0, y=[ 1.  1.  1. ...,  1.  1.  1.], z=[{'a': None}, <class '__main__.A'>]
```
