import subprocess
import sys
import os

# Find the absolute paths for g++ and valgrind
try:
    gpp_path = subprocess.check_output(['which', 'g++']).decode().strip()
    valgrind_path = subprocess.check_output(['which', 'valgrind']).decode().strip()
except subprocess.CalledProcessError:
    print("Error: Unable to find g++ or valgrind in the system's PATH.")
    sys.exit(1)

# Check if g++ and valgrind are found in the system's PATH
if not os.access(gpp_path, os.X_OK):
    print("g++ not found in the system's PATH.")
    sys.exit(1)

if not os.access(valgrind_path, os.X_OK):
    print("valgrind not found in the system's PATH.")
    sys.exit(1)

zero_commit = "0000000000000000000000000000000000000000"

# Flag to track if memory leaks are detected
memory_leak_detected = False

for line in sys.stdin:
    old_sha, new_sha, refname = line.strip().split()

    # Check if it's a new branch or a branch deletion
    if old_sha == zero_commit:
        # New branch, fetch all the changes
        changes = subprocess.check_output(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', new_sha]).decode().strip()
    else:
        # Existing branch, fetch only the new changes since the last push
        changes = subprocess.check_output(['git', 'diff', '--name-only', old_sha, new_sha]).decode().strip()

    # Check for C++ files in the changes
    if any(filename.endswith('.cpp') for filename in changes.split('\n')):
        print("C++ files detected. Running Valgrind to check for memory leaks...")

        # Loop through C++ files and perform Valgrind memory profiling
        for filename in changes.split('\n'):
            if filename.endswith('.cpp'):
                # Compile the C++ file and run Valgrind
                subprocess.run([gpp_path, '-g', filename, '-o', f'{filename}.out'])
                subprocess.run([valgrind_path, '--leak-check=full', f'./{filename}.out'])

                # Check if Valgrind detected any memory leaks
                if subprocess.run([valgrind_path, '--leak-check=full', f'./{filename}.out']).returncode != 0:
                    memory_leak_detected = True

                # Clean up the compiled file
                os.remove(f'{filename}.out')

# Check if memory leaks were detected and exit with appropriate status
if memory_leak_detected:
    print("Memory leak detected. Rejecting the push/merge.")
    sys.exit(1)

sys.exit(0)
