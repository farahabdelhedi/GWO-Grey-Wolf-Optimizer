# fitness.py
import numpy as np

def sphere(x):
    x = np.array(x)
    return np.sum(x**2)

def rastrigin(x):
    x = np.array(x)
    n = len(x)
    return 10*n + np.sum(x**2 - 10 * np.cos(2*np.pi*x))

def rosenbrock(x):
    x = np.array(x)
    return np.sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)
