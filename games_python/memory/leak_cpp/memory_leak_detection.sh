#!/bin/bash

# which g++
# which valgrind

g++="/usr/bin/g++"
valgrind="/usr/bin/valgrind"

zero_commit="0000000000000000000000000000000000000000"

while read old_sha new_sha refname; do
  # Check if it's a new branch or a branch deletion
  if [[ $old_sha == $zero_commit ]]; then
    # New branch, fetch all the changes
    changes=$(git diff-tree --no-commit-id --name-only -r $new_sha)
  else
    # Existing branch, fetch only the new changes since the last push
    changes=$(git diff --name-only $old_sha $new_sha)
  fi

  # Check for C++ files in the changes
  if echo "$changes" | grep -q '.cpp$'; then
    echo "C++ files detected. Running Valgrind to check for memory leaks..."

    # Loop through C++ files and perform Valgrind memory profiling
    for file in $(echo "$changes" | grep '.cpp$'); do
      # Compile the C++ file and run Valgrind
      $g++ -g $file -o $file.out
      $valgrind --leak-check=full ./$file.out

      # Clean up the compiled file
      rm $file.out
    done

    # If you want to reject the push/merge if there are memory leaks, uncomment the following line:
    exit 1
  fi
done

exit 0
