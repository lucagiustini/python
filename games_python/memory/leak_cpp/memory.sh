#!/bin/bash

# Find the absolute paths for g++ and valgrind
gpp_path=$(which g++)
valgrind_path=$(which valgrind)

# Check if g++ and valgrind are found in the system's PATH
if [ -x "$gpp_path" ]; then
  g++="$gpp_path"
else
  echo "g++ not found in the system's PATH."
  exit 1
fi

if [ -x "$valgrind_path" ]; then
  valgrind="$valgrind_path"
else
  echo "valgrind not found in the system's PATH."
  exit 1
fi

# Branch names to compare
old_sha="main"
new_sha="update"
memory_leak_detected = false

# Check if it's a new branch or a branch deletion
if [ "$old_sha" == "$zero_commit" ]; then
  # New branch, fetch all the changes
  changes=$(git diff-tree --no-commit-id --name-only -r "$new_sha")
else
  # Existing branch, fetch only the new changes since the last push
  changes=$(git diff --name-only "$old_sha" "$new_sha")
fi

# Check for C++ files in the changes
if echo "$changes" | grep -q '.cpp$'; then
  echo "C++ files detected. Running Valgrind to check for memory leaks..."

  # Loop through C++ files and perform Valgrind memory profiling
  for file in $(echo "$changes" | grep '.cpp$'); do
    # Compile the C++ file and run Valgrind
    #$g++ -g create_leak.cpp -o create_leak
    #valgrind --leak-check=full ./create_leak

    $g++ -g "$file" -o "$file"
    $valgrind --leak-check=full "./$file"

    # Check if Valgrind detected any memory leaks
    if [ $? -ne 0 ]; then
    memory_leak_detected=true
    fi

    # Clean up the compiled file
    # rm $file.out
  done
fi

# Check if memory leaks were detected and exit with appropriate status
if [ "$memory_leak_detected" = true ]; then
  echo "Memory leak detected. Rejecting the push/merge."
  exit 1
fi

exit 0
