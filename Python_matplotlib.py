#Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 9])
ypoints = np.array([0, 2500])

plt.plot(xpoints, ypoints)
plt.show()