import tracemalloc
import subprocess
import time
import test_memory_leak
import gc

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
    

def main():
    
    # using subprocess print the memory usage
    print("########## START #############\n")
    print()
    subprocess.call(['free', '-h'])
    gc.collect()
    print("FREE THE MEMORY")
    print()
    print("################################\n")
    subprocess.call(['free', '-h'])
    print("################################\n")
    time.sleep(1)
    
    print("#################################\n")
    print()
    print("create the memory leak")
    #test_memory_leak.main()
    #test_memory_leak.main()
    
    # Check memory leak
    print("#################################\n")
    print()
    print("Check memory leak")
    memory_leak_check()
    print()
    
    print("################################\n")
    subprocess.call(['free', '-h'])
    print("################################\n")
    gc.collect()
    print("FREE THE MEMORY")
    print()
    print("################################\n")
    subprocess.call(['free', '-h'])
    print("################################\n")
    print()
    

# type the definistion of the main funtion in python
if __name__ == "__main__":
    # Start memory tracing
    print("Starting memory tracing...")
    start_memory_trace()
    #main()
    while True:
        main()
        time.sleep(5)
    
    
# Run the program and check the memory usage
# in background run the command free -h to check the memory usage
# nohup python your_script.py &
# free -h

# Containerize the script: If you are familiar with containerization technologies like Docker, you can package your script and its dependencies into a container image. 
# Then, you can run the container in the background, and it will isolate the execution of the script.

# to stop the script
# ps -ef | grep python
# kill -9 pid
# ps aux | grep your_script.py
# kill <PID> 
# Replace <PID> with the actual process ID you obtained in the previous step.

# pkill -f your_script.py
# testing the memory leak with the script python/games_python/test_memory_leak.py