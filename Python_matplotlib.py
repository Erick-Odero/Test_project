import matplotlib.pyplot as plt  # Import the matplotlib.pyplot library for creating visualizations/plots.
import numpy as np  # Import the numpy library for working with arrays and numerical computations.

xpoints = np.array([0, 9])  # Create a numpy array for the x-axis points: 0 and 9.
ypoints = np.array([0, 2500])  # Create a numpy array for the y-axis points: 0 and 2500.

plt.plot(xpoints, ypoints)  # Plot the x and y points as a line on a graph.
plt.show()  # Display the plot in a window.
