#!/usr/bin/env python3

"""
creates a tensorflow layer that includes L2 regularization
"""
import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    '''
    Args:
        *prev is a tensor containing the output of the previous layer
        *n is the number of nodes the new layer should contain
        *activation is the activation function that should be used on the layer
        *lambtha is the L2 regularization parameter

    Returns: the output of the new layer
    '''
    kernel = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    regularizer = tf.contrib.layers.l2_regularizer(lambtha)
    layer = tf.layers.Dense(units=n, activation=activation,
                            kernel_initializer=kernel,
                            kernel_regularizer=regularizer, name="layer",
                            )
    return layer(prev)
