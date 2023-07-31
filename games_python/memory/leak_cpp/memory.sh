#!/bin/bash

zero_commit="0000000000000000000000000000000000000000"

# print read old_sha new_sha refname


# get all files changed
for file in $(git diff --name-only update main); do
    # only check cpp files
    if [[ "$file" =~ \.cpp$ ]]; then
        # check if file contains memory leak
        if grep -q "new" "$file"; then
            echo "Memory leak detected in $file"
        fi
    fi
done

# how can I execute this script in shell?
# ./memory.sh
