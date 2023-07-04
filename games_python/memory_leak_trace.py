import tracemalloc

tracemalloc.start()
# ... start your application ...

def function_with_memory_leak():
    """
    A function that exhibits a memory leak.
    """
    # Simulating a memory leak by creating a large list
    large_list = [0] * (10**7)  # A list with ten million elements

snapshot1 = tracemalloc.take_snapshot()
# ... call the function leaking memory ...

function_with_memory_leak()

snapshot2 = tracemalloc.take_snapshot()

top_stats = snapshot2.compare_to(snapshot1, 'lineno')

print("[ Top 10 differences ]")
for stat in top_stats[:10]:
    print("{} new KiB {} total KiB {} new {} total memory blocks: ".format(stat.size_diff/1024, stat.size / 1024, stat.count_diff ,stat.count))