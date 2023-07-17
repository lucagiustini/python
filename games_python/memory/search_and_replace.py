import os
import getopt
import sys

action = 'WARNING !!!'

try:
    opts, args = getopt.getopt(sys.argv[1:],"s:",["SWAP="]) # the options of the script
except getopt.GetoptError:
    print('execute_CMD.py --SWAP <on or off> --usersame <username> --password <psw> --command <command_to_execute>')
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-d", "--SWAP"):
        action = arg
        
if action == 'on':
    # The string to search for
    search_string = "#/swapfile"
    # The string to replace the search string with
    replace_string = "/swapfile"
elif action == 'off':
    # The string to search for
    search_string = "/swapfile"
    # The string to replace the search string with
    replace_string = "#/swapfile"

# Open the file in read mode

file = open("/etc/fstab", "r")
file_contents = file.read()
file.close()

print()
print("################################################")
print()

# Replace the search string with the replace string
file_contents = file_contents.replace(search_string, replace_string)

# Open the file in write mode and write the new contents

file = open("/etc/fstab", "w")
file.write(file_contents)
file.close()

print(file_contents)
print()
print("################################################")
print()

# To run the script as root to modify the file, run the following command: 
# $ sudo python3 search_and_replace.py --SWAP on
# $ sudo python3 search_and_replace.py --SWAP off