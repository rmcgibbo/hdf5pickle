hdf5pickle
==========

Fast persistence of Python objects to HDF5 files.

[![Build Status](https://travis-ci.org/rmcgibbo/hdf5pickle.png?branch=master)](https://travis-ci.org/rmcgibbo/hdf5pickle)
[![PyPI Version](https://badge.fury.io/py/hdf5pickle.png)](https://pypi.python.org/pypi/hdf5pickle)
[![Downloads](https://pypip.in/d/hdf5pickle/badge.png)](https://pypi.python.org/pypi/hdf5pickle)

Example
-------

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


Functions
---------
```
Type:       function
String Form:<function dump at 0x19d9d70>
Definition: hdf5pickle.dump(obj, filename, compress=3, complib='blosc')
Docstring:

Fast persistence of an arbitrary Python object into HDF5 files

Parameters
----------
value: any Python object
    The object to store to disk
filename: string
    The name of the file in which it is to be stored.
compress: integer for 0 to 9, optional
    Optional compression level for the data. 0 is no compression.
    Higher means more compression, but also slower read and
    write times. Using a value of 3 is often a good compromise.
complib : str
    Specifies the compression library to be used. Right now, 'zlib' (the
    default), 'lzo', 'bzip2' and 'blosc' are supported.  Additional
    compressors for Blosc like 'blosc:blosclz' ('blosclz' is the default
    in case the additional compressor is not specified), 'blosc:lz4',
    'blosc:lz4hc', 'blosc:snappy' and 'blosc:zlib' are supported too.
    Specifying a compression library which is not available in the
    system issues a FiltersWarning and sets the library to the default
    one.

See Also
--------
hdf5pickle.load

Type:       function
String Form:<function load at 0x19d9de8>
Definition: hdf5pickle.load(filename)
Docstring:
Reconstruct a Python object from a file persisted with h5pickle.dump

Parameters
-----------
filename: string
    The name of the file from which to load the object

Returns
-------
result: any Python object
    The object stored in the file.

See Also
--------
hdf5pickle.dump
```


