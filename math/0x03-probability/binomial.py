#!/usr/bin/env python3
"""
Initialize binomial
"""


class Binomial:
    """ calculate binomial """
    def __init__(self, data=None, n=1, p=0.5):
        self.data = data
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p >= 1 or p <= 0:
                raise ValueError("p must be greater than 0 and less than 1")

            else:
                self.p = float(p)
                self.n = int(n)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 3:
                raise ValueError("data must contain multiple values")
            else:
                S = sum(data)
                mean = S / len(data)
                varience = 0
                for i in data:
                    varience += (i - mean) ** 2 / len(data)
                p = 1 - (varience / mean)
                n = mean / p
                self.n = round(n)
                self.p = float(mean / self.n)