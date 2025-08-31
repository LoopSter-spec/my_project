#!/bin/bash

# This is a comment. It's not executed.
echo "Hello, World from my first Bash script!"

# Show the current date and time
echo "The current time is: $(date)"

# List all files in the current directory (with details)
echo "Here are the files in this folder:"
ls -l

# Create a new file
touch created_by_script.txt
echo "I created a new file for you!" > created_by_script.txt

# A simple if statement
if [ -f "created_by_script.txt" ]; then
    echo "Success: The file was created!"
else
    echo "Error: The file was not found."
fi

echo "Script finished!"
