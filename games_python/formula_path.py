# Python code​​​​​​‌​‌​​​‌​​‌​‌​​‌​​‌‌‌​‌​‌‌ below
# Use print("messages...") to debug your solution.

import os

def locate_universe_formula():
    file_to_find = "leak_memory.py"
    folder_path = "/home/user/python/games_python/memory"
    for root, dirs, files in os.walk(folder_path):
        if file_to_find in files:
            file_path = os.path.join(root, file_to_find)
            print(file_path)
            return file_path  # Return the path of the file
    print("There's nothing!!!")
    return None

result = locate_universe_formula()