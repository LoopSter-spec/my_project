#!/usr/bin/env python3

# This is a comment in Python
print("Hello, World from my first Python script!")

# Import a module to get the current time
from datetime import datetime
current_time = datetime.now()
print(f"The current time is: {current_time}")

# Import the OS module to interact with the system
import os
print("Here are the files in this folder:")
files = os.listdir() # Gets the list of files in the current directory

for file in files:
    print(f" - {file}")

# Create a new file and write to it
with open('created_by_python.txt', 'w') as f:
    f.write("I created this file using Python!\n")
    f.write(f"The script ran at: {current_time}")

print("I created a new file called 'created_by_python.txt'")

# A simple if statement
if os.path.exists("created_by_python.txt"):
    print("Success: The Python file was created!")
else:
    print("Error: The Python file was not found.")

print("Python script finished!")	
