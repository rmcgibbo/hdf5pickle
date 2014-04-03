.. hdf5pickle documentation master file, created by
   sphinx-quickstart on Wed Apr  2 22:32:08 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to hdf5pickle's documentation!
======================================

Create easily interfaceable representations of Python objects in HDF5
files. The aim of this module is to provide both

    (1) convenient Python object persistence
    (2) compatibility with non-Python applications

Point 2 is useful, for example, if results from numerical
calculations should be easily transferable for example to a non-Python
visualization program. For example, if program state is serialized to
a HDF5 file, it can easily be examined with for example Octave_.

.. _Octave: http://www.octave.org/


Example
-------

::

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



Functions
---------
.. currentmodule:: hdf5pickle
.. autosummary::
    :toctree: generated/

    dump
    load


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

