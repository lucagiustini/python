# create a scritp to diagnostic memory leak
# import the necessary packages

import psutil
import subprocess
import re
import time
import sys
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import tracemalloc

# using tracemalloc print the memory usage

tracemalloc.start(10)
snapshots = tracemalloc.take_snapshot()
time.sleep(1)
snapshots = tracemalloc.take_snapshot()
stats = snapshots.compare_to(snapshots, 'lineno')
for stat in stats[:10]:
    print(stat)
    
def collect_stats(filters = []):        
    #snapshots.append(tracemalloc.take_snapshot())
    # if len is 1, we can't compare to the previous snapshot
    
    if len(snapshots) != 1:
        stats = snapshots[-1].filter_traces(filters).compare_to(snapshots[-2], 'filename')
        for stat in stats[:10]:                
            print("{} new KiB {} total KiB {} new {} total memory blocks: ".format(stat.size_diff/1024, stat.size / 1024, stat.count_diff ,stat.count))                
            for line in stat.traceback.format():                    
                print(line)
        
# using psutil print the memory usage

print(psutil.virtual_memory())
print(psutil.swap_memory())

# using subprocess print the memory usage

subprocess.call(['free', '-h'])

# call collect_stats function

collect_stats()

# function that allow to write in the file.txt the Packets Lost

def writeMemoryUsage():
    # Open the file in read mode
    file = open("memory_usage.txt", "w")
    file.write("memory usage")
    file.close()
    
    # Open the file in read mode
    file = open("memory_usage2.txt", "w")
    file.write("memory usage2")
    file.close()

# function that allow to search in the file.txt the Packets Lost

def getMemoryUsage():
    with open('memory_usage.txt', 'r') as f:
        memory_usage = re.search(r'(\d+)% memory usage', f.read())
        if memory_usage:
            return int(memory_usage.group(1))
        else:
            return None
        
def getMemoryUsage2():
    with open('memory_usage2.txt', 'r') as f:
        memory_usage2 = re.search(r'(\d+)% memory usage', f.read())
        if memory_usage2:
            return int(memory_usage2.group(1))
        else:
            return None

# function that plot the memory usage

def plotMemoryUsage():
    matplotlib.use( 'tkagg' )
    # Create data
    x = np.arange(0, 10, 0.1);
    y = np.sin(x);
    # Plot the data
    plt.plot(x, y, label='sin(x)')
    # Add a legend
    plt.legend()
    # Show the plot
    plt.show()
    
writeMemoryUsage()
getMemoryUsage()
plotMemoryUsage()

# diagnostic memory leak

# 1. check the memory usage before the execution of the script

# 2. check the memory usage after 1 minute

# 3. check the memory usage after 2 minute
