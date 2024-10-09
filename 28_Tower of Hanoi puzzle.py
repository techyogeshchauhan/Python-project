def tower_of_hanoi(n, source, auxiliary, destination):
    """
    Solves the Tower of Hanoi puzzle.
    
    Parameters:
        n (int): Number of disks.
        source (str): The source rod.
        auxiliary (str): The auxiliary rod.
        destination (str): The destination rod.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    
    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Move the n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)

# Number of disks
n = 3

# Calling the function to solve Tower of Hanoi puzzle
tower_of_hanoi(n, 'A', 'B', 'C')
