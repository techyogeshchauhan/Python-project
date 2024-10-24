import numpy as np
import matplotlib.pyplot as plt

# Generate values for the x-axis (0 to 4π)
x = np.linspace(0, 4 * np.pi, 1000)

# Calculate the cosine of the x values
y = np.cos(x)

# Plotting the cosine wave
plt.plot(x, y, label='Cosine Wave', color='r')

# Adding title and labels
plt.title('Cosine Wave Graph')
plt.xlabel('x values (radians)')
plt.ylabel('cos(x)')

# Adding a grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
