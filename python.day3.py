# Task-7 create text file to get current time stamp
from datetime import datetime

# Get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# Create a file object with extension
file_name = f"{current_datetime}.txt"

try:
    with open(file_name, "w") as file:
        file.write("Hello, this is The  content for the file.")
        print(f"File '{file_name}' created successfully.")
except IOError:
    print(f"Error creating or writing to file '{file_name}'.")

# Read file content
def read_file_content(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

read_file_content(file_name)



