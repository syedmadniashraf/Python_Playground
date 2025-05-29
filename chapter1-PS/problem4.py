# 4. Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

import os

# Specify the directory path.
directory = '/'

# Get the list of files and directories in the specified directory.
entries = os.listdir(directory)

# Iterate over the entries and print each one.
for entry in entries:
    print(entry)
