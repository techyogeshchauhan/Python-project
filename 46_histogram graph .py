import matplotlib.pyplot as plt

def plot_histogram(data, bins, title, x_label, y_label):
    """
    Plots a histogram using the provided data.
    
    Parameters:
        data (list): A list of numerical data to plot.
        bins (int): Number of bins (intervals) for the histogram.
        title (str): Title of the histogram.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
    """
    # Plotting the histogram
    plt.hist(data, bins=bins, color='blue', edgecolor='black')
    
    # Adding title and labels
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    # Display the histogram
    plt.show()

# Example data to plot
data = [12, 15, 13, 10, 12, 14, 17, 18, 16, 19, 20, 10, 15, 14, 13, 18, 19, 20, 21, 22, 23, 25]

# Number of bins
bins = 5

# Call the function to plot the histogram
plot_histogram(data, bins, title="Sample Histogram", x_label="Data Ranges", y_label="Frequency")
