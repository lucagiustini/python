import tracemalloc

s = 0

def start_memory_trace():
    tracemalloc.start()

def stop_memory_trace():
    tracemalloc.stop()

def memory_leak_check():
    # Take a memory snapshot
    snapshot = tracemalloc.take_snapshot()

    # Display the details of a specific memory block
    
    top_stats = snapshot.statistics('lineno')

    print("Memory allocation trace:")
    global s
    if not s:
        s = tracemalloc.take_snapshot()
        print("taken snapshot\n")
    else:
        lines = []
        top_stats = tracemalloc.take_snapshot().compare_to(s, 'lineno')
        for stat in top_stats[:10]:  # Change the number to display more or fewer entries
            lines.append(str(stat))  
            # KiB = 1024 bytes (https://en.wikipedia.org/wiki/Kibibyte)
            print("{} new KiB {} total KiB {} new {} total memory blocks, {}: ".format(stat.size_diff/1024, stat.size/1024, stat.count_diff ,stat.count, stat.traceback.format()))
        return "\n".join(lines)