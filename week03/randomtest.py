import numpy as np
import matplotlib.pyplot as plt
list = list(range(10))

print(list)

liste = np.random.default_rng()

print(liste.random())

print(liste.integers(19))

liste = np.random.default_rng(seed = 42)

print(liste.random())


rng = np.random.default_rng()
n, p = 10, .5  # number of trials, probability of each trial
s = rng.binomial(n, p, 10000000)

plt.hist(s)
plt.show()