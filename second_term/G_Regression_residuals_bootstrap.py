import numpy as np
import random


def bootstrap(X : np.ndarray, y : np.ndarray, reg, n : int):
    '''Calculates mean and variance of regression coeffitients using residuals bootstrapping.
    X - explanatory variable values
    y - response variable values
    reg - Model class object
    n - number of bootstrap cycles

    Outputs two np.ndarray values -- mean and variance respectively'''
    random.seed()
    coefs = []
    reg.initialize(X, y)
    for _ in range(n):
        y_new = np.array([i + random.choice(reg.error) for i in reg.y])
        reg.refit(y_new)
        coefs.append(reg.params)
    coefs = np.array(coefs)
    return coefs.mean(axis=0), coefs.var(axis=0)