#!/usr/bin/env python3
"""
* X is the numpy.ndarray of shape (d, nx) to normalize
* d is the number of data points
* nx is the number of features
* m is a numpy.ndarray of shape (nx,)
  that contains the mean of all features of X
* s is a numpy.ndarray of shape (nx,)
  that contains the standard deviation of all features of X
Returns: The normalized X matrix
"""


def normalize(X, m, s):
    """ normalize data"""
    return (X-m) / s
