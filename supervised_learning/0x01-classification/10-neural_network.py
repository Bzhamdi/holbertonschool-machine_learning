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
        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """The weights vector for the hidden layer"""
        return self.__W1

    @property
    def b1(self):
        """The bias for the hidden layer. """
        return self.__b1

    @property
    def A1(self):
        """ The activated output for the hidden layer """
        return self.__A1

    @property
    def W2(self):
        """ The weights vector for the output neuron"""
        return self.__W2

    @property
    def b2(self):
        """The bias for the output neuron. """
        return self.__b2

    @property
    def A2(self):
        """ The activated output for the output neuron (prediction). """
        return self.__A2

    def forward_prop(self, X):
        """Calculates the forward propagation of the neural network
        X is a numpy.ndarray with shape (nx, m) that contains the input data
        nx is the number of input features to the neuron
        m is the number of examples
        """
        z1 = np.matmul(self.W1, X) + self.__b1
        Sigmoid_a1 = 1 / (1 + np.exp(-z1))
        self.__A1 = Sigmoid_a1
        z2 = np.matmul(self.W2, self.__A1) + self.__b2
        Sigmoid_a2 = 1 / (1 + np.exp(-z2))
        self.__A2 = Sigmoid_a2
        return self.__A1, self.__A2
