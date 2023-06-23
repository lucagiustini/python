import os

# Open the file

file = open("/etc/fstab", "r")
file_contents = file.read()
file.close()

print(file_contents)
print()
print()

# The string to search for
search_string = "#/swapfile"

# The string to replace the search string with
replace_string = "/swapfile"

# Replace the search string with the replace string
file_contents = file_contents.replace(search_string, replace_string)

# write the file contents to a new file

file = open("/etc/fstab", "w")
file.write(file_contents)
file.close()

print(file_contents)

# To run the script as root to modify the file, run the following command: $ sudo python3 search_and_replace.py