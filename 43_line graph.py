import matplotlib.pyplot as plt

def plot_line_graph(x_values, y_values, title, x_label, y_label):
    """
    Plots a line graph using the provided x and y values.
    
    Parameters:
        x_values (list): A list of values for the x-axis.
        y_values (list): A list of values for the y-axis.
        title (str): Title of the graph.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
    """
    plt.plot(x_values, y_values, marker='o', color='b', linestyle='-', linewidth=2)
    
    # Adding title and labels
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    # Display the graph
    plt.show()

# Example data to plot
x_values = [1, 2, 3, 4, 5, 6]
y_values = [2, 3, 5, 7, 11, 13]

# Call the function to plot the graph
plot_line_graph(x_values, y_values, title="Prime Numbers Line Graph", x_label="X Values", y_label="Y Values")
