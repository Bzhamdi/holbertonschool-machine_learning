#!/usr/bin/env python3
"""
class NeuralNetwork that defines a neural
network with one hidden layer
performing binary classification
"""
import numpy as np


class NeuralNetwork:
    """
    class NeuralNetwork
    with one hidden layer
    performing binary classification
    """
    def __init__(self, nx, nodes):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        elif nx <= 0:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        elif nodes <= 0:
            raise ValueError("nodes must be a positive integer")
        self.W1 = np.random.normal(size=(nodes, nx))
        self.b1 = np.zeros((nodes, 1))
        self.A1 = 0
        self.W2 = np.random.normal(size=(1, nodes))
        self.b2 = 0
        self.A2 = 0
