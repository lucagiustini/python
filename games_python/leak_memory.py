import tracemalloc
import subprocess
import time

s = 0

def start_memory_trace():
    tracemalloc.start()

def stop_memory_trace():
    tracemalloc.stop()

def memory_leak_check():
    snapshot = tracemalloc.take_snapshot()
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
            top_stats = tracemalloc.take_snapshot().compare_to(s, 'lineno')
            lines.append(str(stat))  
            # KiB = 1024 bytes (https://en.wikipedia.org/wiki/Kibibyte)
            print("{} new KiB {} total KiB {} new {} total memory blocks: ".format(stat.size_diff/1024, stat.size/1024, stat.count_diff ,stat.count))
        return "\n".join(lines)

def main():
    
    # Check memory leak
    memory_leak_check()
    print()
    
    # using subprocess print the memory usage
    #subprocess.call(['free', '-h'])
    #print()
    
    time.sleep(1)

# type the definistion of the main funtion in python
if __name__ == "__main__":
    # Start memory tracing
    start_memory_trace()
    
    # using subprocess print the memory usage
    subprocess.call(['free', '-h'])
    print()
    while True:
        main()
    
    
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