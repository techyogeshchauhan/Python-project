import numpy as np
import matplotlib.pyplot as plt

# Coefficients of the quadratic equation y = ax^2 + bx + c
a = 1
b = -3
c = 2

# Generate x values (-10 to 10)
x = np.linspace(-10, 10, 400)

# Calculate the quadratic equation y = ax^2 + bx + c
y = a * x**2 + b * x + c

# Plotting the quadratic graph
plt.plot(x, y, label=f'Quadratic Curve: {a}x² + {b}x + {c}', color='r')

# Adding title and labels
plt.title('Quadratic Graph')
plt.xlabel('x values')
plt.ylabel('y values')

# Adding a grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
