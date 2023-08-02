import os

def locate_universe_formula(path):
    file_to_find = ".cpp"
    folder_path = "/home/user/" + path
    cpp_files = []

    for root, dirs, files in os.walk(folder_path):
        # Filter out hidden directories that start with "."
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        # Filter out paths that contain "/lib"
        dirs[:] = [d for d in dirs if not d.endswith('lib')]

        for file in files:
            if file.endswith(file_to_find):
                file_path = os.path.join(root, file)
                cpp_files.append(file_path)
                #print(file_path)
                #return file_path
            

    if cpp_files:
        for file_path in cpp_files:
            print(file_path)
        return cpp_files
    else:
        print("There are no files with the .cpp extension in the specified directory.")
        return None

#result = locate_universe_formula("python/")

