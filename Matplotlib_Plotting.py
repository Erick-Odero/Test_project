# Drawing two points in a diagram with different coordinates
import matplotlib.pyplot as plt # Import the matplotlib.pyplot library for creating visualizations/plots.
import numpy as np # Import the numpy library for working with arrays and numerical computations.

xpoints = np.array([1,9]) # Create a numpy array for the x-axis points: 1 and 9.
ypoints = np.array([4,11])# Create a numpy array for the y-axis points: 4 and 11.
plt.plot(xpoints, ypoints, 'o') # Plot the x and y points as individual markers ('o' specifies circle markers) without connecting them with a line.
plt.show() #Display the plot