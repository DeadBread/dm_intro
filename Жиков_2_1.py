import numpy as np

def func1(x):
    if (x > 0):
        return x
    else:
        return 0.01 * x

vectorized1 = np.vectorize(func1)

print vectorized1(np.array([1,2,-3,4,-2], dtype = 'double'))

def func2(x, sigma):
    rand = np.random.normal(sigma)
    return max(0.0, x + rand)

vectorized2 = np.vectorize(func2, excluded = ['sigma'])

print vectorized2(np.array([1,2,3]),1)
