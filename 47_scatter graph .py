import matplotlib.pyplot as plt

def plot_scatter_graph(x_values, y_values, title, x_label, y_label):
    """
    Plots a scatter graph using the provided x and y values.
    
    Parameters:
        x_values (list): A list of values for the x-axis.
        y_values (list): A list of values for the y-axis.
        title (str): Title of the scatter plot.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
    """
    plt.scatter(x_values, y_values, color='blue', marker='o')

    # Adding title and labels
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    # Display the scatter plot
    plt.show()

# Example data to plot
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Call the function to plot the scatter graph
plot_scatter_graph(x_values, y_values, title="Sample Scatter Plot", x_label="X Values", y_label="Y Values")
