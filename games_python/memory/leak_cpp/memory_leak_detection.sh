import subprocess
import shutil
import os
import formula_path

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
memory_leak_detected = False

def process_files(file_list):
    for filename in file_list:
        binary_file = os.path.splitext(filename)[0]
        # Rest of your code to process the file goes here
        return binary_file

# Example usage
# file_list = ["file1.cpp", "file2.txt", "file3.py"]
# process_files(file_list)

# Check if it's a new branch or a branch deletion
try:
    subprocess.run(['git', 'rev-parse', old_sha], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.CalledProcessError:
    # New branch, fetch all the changes
    changes = subprocess.run(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', new_sha], capture_output=True, text=True).stdout.strip()
else:
    # Existing branch, fetch only the new changes since the last push
    changes = subprocess.run(['git', 'diff', '--name-only', old_sha, new_sha], capture_output=True, text=True).stdout.strip()

# Check for C++ files in the changes
if any(filename.endswith('.cpp') for filename in changes.split('\n')):
    print("C++ files detected. Running Valgrind to check for memory leaks...")
    print(changes)
    print('######################')
    
    # Loop through C++ files and perform Valgrind memory profiling
    for filename in changes.split('\n'):
        if filename.endswith('.cpp'):
            #filename = formula_path.locate_universe_formula("python/games_python/")
            filename = "/home/user/python/" + filename
            print(filename)
            try:
                # Remove the .cpp extension to use it for the output binary file name
                # process_files(changes)
                binary_file = os.path.splitext(filename)[0]

                # Compile the C++ file and run Valgrind
                subprocess.run([gpp_path, '-g', filename, '-o', binary_file], check=True)

                # Run Valgrind to check for memory leaks
                valgrind_output = subprocess.run([valgrind_path, '--leak-check=full', f'./{filename}'], capture_output=True, text=True)
                print('######################')
                print(valgrind_output.stdout)
                # Write the Valgrind output to 'RESULTS.txt'
                with open('RESULTS.txt', 'w') as f:
                    f.write(valgrind_output.stdout)
                
                # Clean up the compiled file (if necessary)
                # subprocess.run(['rm', f'{filename}.out'], check=True)
                
                # Check if Valgrind detected any memory leaks
                if "Memory allocated:" in valgrind_output.stdout:
                    memory_leak_detected = True

            except subprocess.CalledProcessError as e:
                print(f"Error compiling or running '{filename}': {e}")
                # Optionally handle the error or continue with the next file

# Check if memory leaks were detected and exit with appropriate status
if memory_leak_detected:
    print("Memory leak detected. Rejecting the push/merge.")
    exit(1)

exit(0)
