import subprocess
import shutil

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

    # Loop through C++ files and perform Valgrind memory profiling
    for filename in changes.split('\n'):
        if filename.endswith('.cpp'):
            try:
                # Compile the C++ file
                subprocess.run([gpp_path, '-g', filename, '-o', filename], check=True)
                
                # Run Valgrind to check for memory leaks
                subprocess.run([valgrind_path, '--leak-check=full', f'./{filename}'], check=True)
                
                # Clean up the compiled file (if necessary)
                # subprocess.run(['rm', f'{filename}.out'], check=True)
                
            except subprocess.CalledProcessError as e:
                print(f"Error compiling or running '{filename}': {e}")
                # Optionally handle the error or continue with the next file

# No need to explicitly check for memory leaks since subprocess.run with check=True raises an exception if there are any issues.

exit(0)
