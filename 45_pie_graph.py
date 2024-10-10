import matplotlib.pyplot as plt

def plot_pie_chart(categories, values, title):
    """
    Plots a pie chart using the provided categories and values.
    
    Parameters:
        categories (list): A list of categories (labels).
        values (list): A list of values corresponding to each category.
        title (str): Title of the pie chart.
    """
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    
    # Equal aspect ratio ensures that the pie is drawn as a circle.
    plt.axis('equal')  
    plt.title(title)
    
    # Display the pie chart
    plt.show()
    

# Example data for the pie chart
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [20, 35, 25, 20]

# Call the function to plot the pie chart
plot_pie_chart(categories, values, title="Sample Pie Chart")
