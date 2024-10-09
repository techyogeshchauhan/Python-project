import matplotlib.pyplot as plt

def plot_bar_graph(categories, values, title, x_label, y_label):
    """
    Plots a bar graph using the provided categories and values.
    
    Parameters:
        categories (list): A list of categories for the x-axis.
        values (list): A list of values for the y-axis.
        title (str): Title of the graph.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
    """
    plt.bar(categories, values, color='green')
    
    # Adding title and labels
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    # Display the bar graph
    plt.show()

# Example data to plot
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [10, 24, 36, 40, 55]

# Call the function to plot the bar graph
plot_bar_graph(categories, values, title="Sample Bar Graph", x_label="Categories", y_label="Values")
