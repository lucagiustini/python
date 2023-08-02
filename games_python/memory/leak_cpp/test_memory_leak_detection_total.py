import subprocess
import shutil
import os
import re
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
test_memory_leak_detected = False
NO_memory_leak_detected = "OH MIO DIO"
fixed_path = "python/"

files = formula_path.locate_universe_formula(fixed_path)
print(files)

#def test_process_files():
# Check for C++ files in the changes
if any(filename.endswith('.cpp') for filename in files):
    print("C++ files detected. Running Valgrind to check for memory leaks...")
    #print(changes)
    #print('######################')
    
    # Loop through C++ files and perform Valgrind memory profiling
    for filename in files:
        if filename.endswith('.cpp'):
            filename = filename
            print('*****************')
            print(filename)
            print('*****************')
            try:
                # Remove the .cpp extension to use it for the output binary file name
                #binary_file = process_files(changes)
                binary_file = os.path.splitext(filename)[0]
                print('*****************')
                print(binary_file)
                print('*****************')
                # Compile the C++ file and run Valgrind
                compile_result = subprocess.run([gpp_path, '-g', filename, '-o', binary_file], check=True)
                #print('######################')
                #print(compile_result)
                # Run Valgrind to check for memory leaks
                # valgrind_output = subprocess.run([valgrind_path, '--leak-check=full', f'./{filename}'], capture_output=True, text=True)
                print(valgrind_path)
                valgrind_output = subprocess.run([valgrind_path, '--leak-check=full', '--show-leak-kinds=all', '--track-origins=yes', '--verbose', '--log-file=valgrind-out.txt', binary_file], capture_output=True, text=True)
                # Run the compiled C++ executable
                #subprocess.run(["valgrind", "--leak-check=full", "--show-leak-kinds=all", "--track-origins=yes", "--verbose", "--log-file=valgrind-out.txt", "./create_leak"])
    
                # print the output of last command
                #subprocess.run(["cat", "valgrind-out.txt"])
                # /usr/bin/valgrind --leak-check=full ./home/user/python/games_python/memory/leak_cpp/OKOKOK
                print('######################')
                print(valgrind_output.stdout)
                # Write the Valgrind output to 'RESULTS.txt'
                with open('valgrind-out.txt', 'r') as f:
                    #Packets_Lost_LIMIT = re.search(r'(\d+)% packet loss', f.read())
                    #print(NO_memory_leak_detected)
                    NO_memory_leak_detected = re.search(r'All heap blocks were freed -- no leaks are possible', f.read())
                    #print(NO_memory_leak_detected)
                    if NO_memory_leak_detected:
                        print('Memory leak NOOOOOOOOOOOOOOOOOOOOO detected')
                        test_memory_leak_detected = False
                    else:
                        print('Memory leak detected')
                        test_memory_leak_detected = True
                        
                # Check if memory leaks were detected and exit with appropriate status
                if test_memory_leak_detected == True:
                    print("Memory leak detected. Rejecting the push/merge.")
                    assert False
                    #exit(1)
                else:
                    print("No memory leaks detected. Push/Merge successful.")
                    assert True
                    #exit(0)
                #
                # Clean up the compiled file (if necessary)
                # subprocess.run(['rm', f'{filename}.out'], check=True)
                
                # Check if Valgrind detected any memory leaks
                #if "possibly lost: " in valgrind_output.stdout:
                #    memory_leak_detected = True

            except subprocess.CalledProcessError as e:
                print(f"Error compiling or running '{filename}': {e}")
                # Optionally handle the error or continue with the next file

