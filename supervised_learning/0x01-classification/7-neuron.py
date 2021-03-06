#!/usr/bin/env python3
"""
the Neuron
"""

import numpy as np
import matplotlib.pyplot as plt


class Neuron:
    """ the Neuron """
    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        elif nx <= 0:
            raise ValueError("nx must be a positive integer")
        else:
            self.__W = np.random.normal(size=(1, nx))
            self.__b = 0
            self.__A = 0

    @property
    def W(self):
        """The weights vector for the neuron"""
        return self.__W

    @property
    def b(self):
        """The bias for the neuron """
        return self.__b

    @property
    def A(self):
        """ The activated output of the neuron (prediction) """
        return self.__A

    def forward_prop(self, X):
        """ Neuron Forward Propagation
        X is a numpy.ndarray with shape (nx, m) that contains the input data
        """
        z = np.matmul(self.W, X) + self.__b
        Sigmoid_a = 1 / (1 + np.exp(-z))
        self.__A = Sigmoid_a
        return self.__A

    def cost(self, Y, A):
        """
        cost of the model using logistic regression
        """
        nx, m = Y.shape
        loss = - (Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        sumloss = np.sum(loss)
        cost = (1 / m) * sumloss
        return cost

    def evaluate(self, X, Y):
        """ evaluate output 0 or 1"""
        Sigmoid_a = self.forward_prop(X)
        pred_evalute = np.where(Sigmoid_a < 0.5, 0, 1)
        cost = self.cost(Y, Sigmoid_a)
        return pred_evalute, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """gradient_descent
        """
        nx, m = Y.shape
        dz = A - Y
        dw = (1/m) * np.sum(dz * X, axis=1)
        db = (1/m) * np.sum(dz)
        self.__W -= (dw * alpha)
        self.__b -= (db * alpha)
        return self.__W, self.__b

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True,
              graph=True, step=100):
        """
        Returns the evaluation of the training data after
        iterations of training have occurred
        used:
        -forward_prop
        -gradient_descent
        and ~ evaluate

        """
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        elif iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        elif not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if verbose or graph:
            if type(step) is not int:
                raise TypeError("step must be an integer")
            if step < 0 or step > iterations:
                raise ValueError("step must be positive and <= iterations")
        xValue = []
        yValue = []
        for i in range(iterations+1):
            self.__A = self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A, alpha)
            cost = self.cost(Y, self.__A)
            if verbose:
                if (i < 1 or i % step == 0):
                    print("Cost after {} iterations: {}".format(i, cost))
                    xValue.append(i+step)
                    yValue.append(cost)
        if graph is True:
            plt.title('Training Cost')
            plt.ylabel('cost')
            plt.xlabel('iteration')
            plt.plot(xValue, yValue)
            plt.show()
        return self.evaluate(X, Y)
