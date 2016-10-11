# -*- coding: utf-8 -*-
"""
Plot of the Ascombe's quartet

@author: Nicolas Guarin-Zapata
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

data = np.loadtxt("../data/ascombe.csv", delimiter=",")
X = data[:, :4]
Y = data[:, 4:]

plt.figure(figsize=(10, 6))
for k in range(4):
    plt.subplot(2, 2, k + 1)
    plt.plot(X[:, k], Y[:, k], 'ok')
    plt.plot([2, 20], [4, 13])
    plt.xlabel(r"$x_{%i}$" % k)
    plt.ylabel(r"$y_{%i}$" % k)
    plt.axis([2, 20, 2, 14])

plt.savefig("ascombe.svg", bbox_inches="tight")
plt.show()