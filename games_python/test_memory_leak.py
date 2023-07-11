import tracemalloc
import psutil
import subprocess

def create_large_list():
    # A function that creates a large list to simulate potential memory leak.
    large_list = [i for i in range(10**6)]  # A list with one million elements
    print("################################\n")
    print("Function create_large_list() called.\n")
    print("################################\n")
    return large_list

def main():
    
    # Simulate potential memory leak
    large_list = create_large_list()
    print()
    

# type the definistion of the main funtion in python
if __name__ == "__main__":
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