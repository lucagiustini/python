#!/bin/bash

zero_commit="0000000000000000000000000000000000000000"

while read old_sha new_sha refname; do
  # Check if it's a new branch or a branch deletion
  if [[ $old_sha == $zero_commit ]]; then
    # New branch, fetch all the changes and check for your_application.cpp
    changed_files=$(git diff --name-only $new_sha)
  else
    # Existing branch, fetch only the new changes since the last push
    changed_files=$(git diff --name-only $old_sha $new_sha)
  fi

  # Check if your_application.cpp is among the changed files
  if echo "$changed_files" | grep -q '^your_application.cpp$'; then
    echo "New your_application.cpp file detected. Running tests and checking for memory leaks..."
    # Add your actions here, e.g., compiling, running tests, and using Valgrind
    # ...

    # If you want to reject the push if there are issues, uncomment the following line:
    # exit 1
  fi
done

exit 0
