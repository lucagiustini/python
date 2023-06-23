# Python code​​​​​​‌​‌​​​‌​​‌​‌​​‌​​‌‌‌​‌​‌‌ below
# Use print("messages...") to debug your solution.

import os

def locate_universe_formula():
    file_to_find = "universe-formula"
    folder_path = "/tmp/documents/"
    for root, dirs, files in os.walk(folder_path):
        if file_to_find in files:
            file_path = os.path.join(root, file_to_find)
            return file_path  # Return the path of the file
    return None

result = locate_universe_formula()