import numpy as np
import matplotlib.pyplot as plt

# Generate x values (0 to 10)
x = np.linspace(0, 10, 1000)

# Calculate the exponential of x (e^x)
y = np.exp(x)

# Plotting the exponential graph
plt.plot(x, y, label='Exponential Curve', color='m')

# Adding title and labels
plt.title('Exponential Graph')
plt.xlabel('x values')
plt.ylabel('exp(x)')

# Adding a grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
