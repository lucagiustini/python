import subprocess
import shutil
import os
import re

# Find the absolute paths for g++ and valgrind
gpp_path = shutil.which('g++')
valgrind_path = shutil.which('valgrind')

# Check if g++ and valgrind are found in the system's PATH
if not gpp_path:
    print("g++ not found in the system's PATH.")
    exit(1)

if not valgrind_path:
    print("valgrind not found in the system's PATH.")
    exit(1)

# Branch names to compare
old_sha = "main"
new_sha = "update"

# Initialize variables
test_memory_leak_detected = False
NO_memory_leak_detected = ""
fixed_path = "/home/user/python/"

# Check if it's a new branch or a branch deletion
try:
    subprocess.run(['git', 'rev-parse', old_sha], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.CalledProcessError:
    # New branch, fetch all the changes
    changes = subprocess.run(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', new_sha], capture_output=True, text=True).stdout.strip()
else:
    # Existing branch, fetch only the new changes since the last push
    changes = subprocess.run(['git', 'diff', '--name-only', old_sha, new_sha], capture_output=True, text=True).stdout.strip()

def test_process_files():
    # Check for C++ files in the changes
    if any(filename.endswith('.cpp') for filename in changes.split('\n')):
        print("C++ files detected. Running Valgrind to check for memory leaks...")
        
        # Loop through C++ files and perform Valgrind memory profiling
        for filename in changes.split('\n'):
            if filename.endswith('.cpp'):
                filename = fixed_path + filename
                print('*****************')
                print(filename)
                print('*****************')
                try:
                    # Remove the .cpp extension to use it for the output binary file name
                    binary_file = os.path.splitext(filename)[0]
                    print('*****************')
                    print(binary_file)
                    print('*****************')
                    # Compile the C++ file and run Valgrind
                    compile_result = subprocess.run([gpp_path, '-g', filename, '-o', binary_file], check=True)
                    # Run Valgrind to check for memory leaks
                    print(valgrind_path)
                    valgrind_output = subprocess.run([valgrind_path, '--leak-check=full', '--show-leak-kinds=all', '--track-origins=yes', '--verbose', '--log-file=valgrind-out.txt', binary_file], capture_output=True, text=True)
                   
                    # print the output of last command
                    #subprocess.run(["cat", "valgrind-out.txt"])
                    
                    print('######################')
                    print(valgrind_output.stdout)
                    # Read the Valgrind output in 'valgrind-out.txt'
                    with open('valgrind-out.txt', 'r') as f:
                        NO_memory_leak_detected = re.search(r'All heap blocks were freed -- no leaks are possible', f.read())
                        if NO_memory_leak_detected:
                            print('No memory leaks detected.')
                            test_memory_leak_detected = False
                        else:
                            print('Memory leak detected.')
                            test_memory_leak_detected = True
                            
                    # Check if memory leaks were detected and exit with appropriate status
                    if test_memory_leak_detected == True:
                        print("Rejecting the push/merge.")
                        assert False
                    else:
                        print("Push/Merge successful.")
                        assert True

                except subprocess.CalledProcessError as e:
                    print(f"Error compiling or running '{filename}': {e}")

