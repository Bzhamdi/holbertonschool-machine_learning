#!/usr/bin/env python3
"""
performs forward propagation over a convolutional layer of a neural network
"""
import numpy as np


def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
    """
    *A_prev is a numpy.ndarray of shape (m, h_prev, w_prev, c_prev)
    containing the output of the previous layer
        m is the number of examples
        h_prev is the height of the previous layer
        w_prev is the width of the previous layer
        c_prev is the number of channels in the previous layer
    *W is a numpy.ndarray of shape (kh, kw, c_prev, c_new)
    containing the kernels for the convolution
        kh is the filter height
        kw is the filter width
        c_prev is the number of channels in the previous layer
        c_new is the number of channels in the output
    *b is a numpy.ndarray of shape (1, 1, 1, c_new) containing the
    biases applied to the convolution
    *activation is an activation function applied to the convolution
    *padding is a string that is either same or valid, indicating
    the type of padding used
    *stride is a tuple of (sh, sw) containing the strides for the convolution
        sh is the stride for the height
        sw is the stride for the width
    """

    kh, kw, c_prev, c_new = W.shape
    m, h_prev, w_prev, c_prev = A_prev.shape

    sh, sw = stride
    if padding == 'valid':
        output_h = int(((h_prev - kh) / sh) + 1)
        output_w = int(((w_prev - kw) / sw) + 1)
        image_padded = np.copy(A_prev)

    elif padding == 'same':

        p_h = int((((h_prev - 1) * sh + kh - h_prev) / 2) + (kh % 2 == 0))
        p_w = int((((w_prev - 1) * sw + kw - w_prev) / 2) + (kw % 2 == 0))

        """ output_h = h and output_w = w"""

        output_h = int(((h_prev - kh + (2 * p_h)) / sh) + 1)
        output_w = int(((w_prev - kw + (2 * p_w)) / sw) + 1)

        image_padded = np.pad(A_prev, ((0, 0), (p_h, p_h),
                              (p_w, p_w), (0, 0)), 'constant')

    output = np.zeros((m, output_h, output_w, c_new))

    for x in range(output_w):
        for y in range(output_h):
            for ch in range(c_new):
                output[:, y, x, ch] = (W[:, :, :, ch] *
                                       image_padded[:, (sh * y): (sh * y) +
                                       kh, (sw * x):  (sw * x) + kw]).sum(
                                        axis=(1, 2, 3))

    return activation(output + b)
