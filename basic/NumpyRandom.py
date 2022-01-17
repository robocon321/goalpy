import numpy as np
from numpy import random

#distribution

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

#shuffle change orginal array and permutatetion no change

arr = np.array([1,2,3,4,5])
random.shuffle(arr)
random.permutation(arr)

#random distribution type

normal = random.normal(loc=1, scale=2, size=(2, 3))
binominal = random.binomial(n=10, p=0.5, size=10)
poisson = random.poisson(lam=2, size=10)
uniform = random.uniform(size=(2, 3))
logistic = random.logistic(loc=1, scale=2, size=(2, 3))
multinomial = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
exponential = random.exponential(scale=2, size=(2, 3))
chi_square = random.chisquare(df=2, size=(2, 3))
rayleigh = random.rayleigh(scale=2, size=(2, 3))
pareto = random.pareto(a=2, size=(2, 3))
zipf = random.zipf(a=2, size=1000)
