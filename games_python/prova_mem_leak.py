import tracemalloc
tracemalloc.start()
s=None

def snap():
    global s
    if not s:
        s = tracemalloc.take_snapshot()
        return "taken snapshot\n"
    else:
        lines = []
        top_stats = tracemalloc.take_snapshot().compare_to(s, 'lineno')
        for stat in top_stats[:5]:
            lines.append(str(stat))  
            print("{} new KiB {} total KiB {} new {} total memory blocks: ".format(stat.size_diff/1024, stat.size / 1024, stat.count_diff ,stat.count))
            #print(lines)
        # print the s values
        print("Memory allocation trace:")
        print("{}".format(s))
        print("daje {}".format(lines))
        print()
        return "\n".join(lines)

def create_large_list():
    """
    A function that creates a large list to simulate potential memory leak.
    """
    large_list = [i for i in range(10**6)]  # A list with one million elements
    return large_list

snap()
create_large_list()
snap()