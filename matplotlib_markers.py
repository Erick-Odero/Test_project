import matplotlib.pyplot as plt  # Import the matplotlib.pyplot library for creating visualizations/plots.
import numpy as np  # Import the numpy library for working with arrays and numerical computations.

ypoints = np.array([4, 5, 9, 10, 56, 9])  # Create a numpy array containing the y-axis values: 4, 5, 9, 10, 56, and 9.

plt.plot(ypoints, marker = 'o')  # Plot the ypoints with circular markers ('o') on the graph. The x-axis values will be automatically set to the indices of the array (0, 1, 2, ...).
plt.show()  # Display the plot in a window.
