import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start, end):
    """
    Finds the shortest path from start node to end node in a weighted graph.
    
    Parameters:
        graph (dict): A dictionary where keys are node names and values are lists of tuples (neighbor, weight).
        start (str): The starting node.
        end (str): The destination node.
    
    Returns:
        tuple: The shortest distance and the shortest path as a list of nodes.
    """
    # Priority queue to hold nodes and their distances
    pq = [(0, start)]
    # Dictionary to hold the shortest distance from start to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Dictionary to store the path (previous node in the optimal path)
    previous_nodes = {node: None for node in graph}
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If the current node's distance is greater than the already known shortest distance, skip it
        if current_distance > distances[current_node]:
            continue
        
        # If we reached the destination, reconstruct the path
        if current_node == end:
            path = []
            while previous_nodes[current_node] is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(start)
            return distances[end], path[::-1]  # Reverse the path to get the correct order
        
        # Check each neighbor of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return float('inf'), []  # If no path is found

# Example graph represented as a dictionary
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 10)],
    'C': [('A', 2), ('B', 5), ('D', 3)],
    'D': [('B', 10), ('C', 3)]
}

# Visualize the graph using networkx
def plot_graph(graph, shortest_path=None):
    G = nx.Graph()
    
    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)
    
    pos = nx.spring_layout(G)  # Layout for visualization
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=15, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
    
    if shortest_path:
        # Highlight the shortest path
        path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=4)

    plt.show()

# Set the start and end node
start_node = 'A'
end_node = 'D'

# Find the shortest path
shortest_distance, shortest_path = dijkstra(graph, start_node, end_node)

# Output the result
print(f"Shortest distance from {start_node} to {end_node} is: {shortest_distance}")
print(f"Shortest path is: {' -> '.join(shortest_path)}")

# Visualize the graph and the shortest path
plot_graph(graph, shortest_path)
