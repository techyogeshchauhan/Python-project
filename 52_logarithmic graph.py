import numpy as np
import matplotlib.pyplot as plt

# Generate x values (1 to 1000)
x = np.linspace(1, 1000, 1000)

# Calculate the natural logarithm of x (ln(x))
y = np.log(x)

# Plotting the logarithmic graph
plt.plot(x, y, label='Logarithmic Curve', color='b')

# Adding title and labels
plt.title('Logarithmic Graph (ln(x))')
plt.xlabel('x values')
plt.ylabel('log(x)')

# Adding a grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
