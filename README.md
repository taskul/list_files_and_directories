Welcome to the list_files_and_directories wiki!

This is a simple program written in Python for Windows. It lists files and directories similar to "ls -l" command in Linux.
The list_files_and_directories also lists the access to files for (r,w,x) similar to "ls -l" command in Linux.
Also included is file sizes and file creation date.

# Adding list_files_and_directories module to Python file
Make sure that the file is in the same folder as the file the list_files_and_directories module is being imported to. 

## import list_files_and_directories as lfd

List current Files and Directories:

## lfd.fidir()

List Files and Directories of other directories:

## lfd.fidir(r'C:\Users\Username\Documents')

The colorrized terminal output works in Code/text Editors, however it doesn't work in CLI like Windows command prompt.
Below is the screenshot of the terminal output

![Screen Shot](https://raw.githubusercontent.com/tastasterone/list_files_and_directories/master/list_and_dir.png)
