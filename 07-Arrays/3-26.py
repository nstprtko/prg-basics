import matplotlib.pyplot as plt
import numpy as np
x = []
y = []

# Generate x values (angle in degrees)
x = np.linspace(0, 360, 361)  # 0 to 360 degrees with 1-degree step

# Compute y values as sin(x) (convert degrees to radians)
y = np.sin(np.radians(x))

# Plot the graph
plt.plot(x, y, label='y = sin(x)', color='green')

# Add labels and title
plt.title('Graph of y = sin(x)')
plt.xlabel('Angle (degrees)')
plt.ylabel('sin(x)')

plt.show()