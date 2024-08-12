
# Task-7 create text file to get current time stamp
# import module
from datetime import datetime

# get current date and time

current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

print("Current date & time : ", current_datetime)

# convert datetime obj to string

str_current_datetime = str(current_datetime)

# create a file object along with extension

file_name = str_current_datetime + ".txt"

file = open(file_name, 'w')

print("File created : ", file.name)

file.close()

# using time module

import time

# ts stores the time in seconds

ts = time.time()

def read_file_content(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

read_file_content(file_name)



