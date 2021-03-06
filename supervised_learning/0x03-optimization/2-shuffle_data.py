#!/usr/bin/env python3
"""
Shuffles the data points in two matrices the same way
"""

import numpy as np


def shuffle_data(X, Y):
    """
    Shuffles the data points in two matrices the same way
    """
    i = np.random.permutation(np.arange(X.shape[0]))
    return X[i], Y[i]
