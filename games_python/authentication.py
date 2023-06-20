import time
import os

WAIT_TIME_FILE = "txt/wait_time.txt"

def ask_password(attempts=3):
    wait_time = get_wait_time()
    
    if attempts == 0:
        print("Maximum number of attempts exceeded. Please try again after {} minutes.".format(wait_time // 60))
        update_wait_time(wait_time * 2)
        time.sleep(wait_time)
        return False
    
    password = input("Enter your password: ")
    
    try:
        password = int(password)
        if password == 1234:
            print("Password is correct")
            update_wait_time(wait_time = 60)
            return True
        else:
            print("Password is incorrect")
            return ask_password(attempts-1)

    except ValueError:
        print("Password is incorrect")
        return ask_password(attempts-1)

def get_wait_time():
    if os.path.exists(WAIT_TIME_FILE):
        with open(WAIT_TIME_FILE, "r") as file:
            wait_time = int(file.read())
    else:
        wait_time = 60  # Default wait time of 1 minute
    
    return wait_time
        
def update_wait_time(wait_time):
    # create a subdirectory if it doesn't exist called txt
    if not os.path.exists("txt"):
        os.makedirs("txt")
    # create in the directory txt a file called wait_time.txt and write the wait_time in it
    with open(WAIT_TIME_FILE, "w") as file: 
        file.write(str(wait_time))

ask_password()

# insert __name__ == "__main__" to run the code only if the file is executed directly
if __name__ == "__main__":
    ask_password()

if __name__ == "authentication":
    print("This is the authentication module")

# do the same thing using os.path.dirname
# import os
# WAIT_TIME_FILE = "txt/wait_time.txt"
#
# def get_wait_time():
#     if os.path.exists(WAIT_TIME_FILE):
#         with open(WAIT_TIME_FILE, "r") as file:
#            wait_time = int(file.read())
#     else:
#        wait_time = 60  # Default wait time of 1 minute
#
#     return wait_time
# 
# def update_wait_time(wait_time):
#     os.makedirs(os.path.dirname(WAIT_TIME_FILE), exist_ok=True)  # Create the "txt" subfolder if it doesn't exist
#     with open(WAIT_TIME_FILE, "w") as file:
#         file.write(str(wait_time))
#
# ask_password()

# Path: games_python/authentication.py