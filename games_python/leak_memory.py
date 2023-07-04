import tracemalloc

def start_memory_trace():
    """
    Start tracing memory allocations.
    """
    tracemalloc.start()

def stop_memory_trace():
    """
    Stop tracing memory allocations.
    """
    tracemalloc.stop()

def display_memory_trace():
    """
    Display memory allocation trace.
    """
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("Memory allocation trace:")

    for stat in top_stats[:10]:  # Change the number to display more or fewer entries
        print(stat)

def create_large_list():
    """
    A function that creates a large list to simulate potential memory leak.
    """
    large_list = [i for i in range(10**6)]  # A list with one million elements
    return large_list

#def main():
# Start memory tracing
start_memory_trace()

# Simulate potential memory leak
large_list = create_large_list()

# Stop memory tracing
stop_memory_trace()

# Display memory trace
display_memory_trace()