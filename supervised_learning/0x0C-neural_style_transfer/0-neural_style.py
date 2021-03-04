#!/usr/bin/env python3
"""neural style transfer"""
import numpy as np
import tensorflow as tf


class NST:
    """neural style transfer"""
    style_layers = ['block1_conv1',
                    'block2_conv1',
                    'block3_conv1',
                    'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        ARGS:
            style_image - the image style reference,
            content_image - the image used as a content reference
            beta - the weight for style cost
        """
        if not isinstance(style_image, np.ndarray) or len(
                style_image.shape) != 3 or style_image.shape[2] != 3:
            raise TypeError(
                'style_image must be a numpy.ndarray with shape (h, w, 3)')
        if not isinstance(content_image, np.ndarray) or len(
                content_image.shape) != 3 or style_image.shape[2] != 3:
            raise TypeError(
                'content_image must be a numpy.ndarray with shape (h, w, 3)')
        if not isinstance(alpha, (int, float)) or alpha < 0:
            raise TypeError('alpha must be a non-negative number')
        if not isinstance(beta, (int, float)) or beta < 0:
            raise TypeError('beta must be a non-negative number')

        tf.enable_eager_execution()
        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

    @staticmethod
    def scale_image(image):
        if not isinstance(image, np.ndarray) or len(
                image.shape) != 3 or image.shape[2] != 3:
            raise TypeError(
                'image must be a numpy.ndarray with shape (h, w, 3)')
        h, w, _ = image.shape
        old = w * h
        if h > w:
            h_new = 512
            w_new = w * h_new / h
        else:
            w_new = 512
            h_new = h * w_new / w

        """Returns a tensor with a length 1 axis inserted at index axis"""
        """image = tf.expand_dims(image, 0)"""
        image = tf.reshape(image, [1, h, w, 3])
        image = tf.image.resize_bicubic(image, (h_new, w_new))
        """rescaled from the range [0, 255] to [0, 1]."""
        image = image / 255
        image = tf.clip_by_value(image, 0, 1)
        return image
