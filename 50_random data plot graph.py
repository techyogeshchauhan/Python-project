import numpy as np
import matplotlib.pyplot as plt

# Generate random data for x and y axes
x = np.random.rand(100)  # 100 random values between 0 and 1 for x
y = np.random.rand(100)  # 100 random values between 0 and 1 for y

# Plotting the random data
plt.scatter(x, y, color='g', label='Random Data')

# Adding title and labels
plt.title('Random Data Plot')
plt.xlabel('Random X values')
plt.ylabel('Random Y values')

# Adding a grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
