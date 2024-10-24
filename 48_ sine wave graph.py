import numpy as np
import matplotlib.pyplot as plt

# Generate values for the x-axis (0 to 4π)
x = np.linspace(0, 4 * np.pi, 1000)

# Calculate the sine of the x values
y = np.sin(x)

# Plotting the sine wave
plt.plot(x, y, label='Sine Wave', color='b')

# Adding title and labels
plt.title('Sine Wave Graph')
plt.xlabel('x values (radians)')
plt.ylabel('sin(x)')

# Adding a grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
