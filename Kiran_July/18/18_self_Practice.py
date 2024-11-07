# 1)What is file handling in Python?
# File handling in Python refers to the operations that can be performed on files, such as reading from and writing to files. It involves using built-in functions and methods to open, read, write, and close files.

# 2) How do you open a file in Python?
# You can open a file using the open() function.
# The syntax is open(filename, mode)
# where mode specifies the purpose of opening the file, such as 'r' for reading, 'w' for writing, 'a' for appending, etc.

file = open('example.txt', 'r')

# 3) What are the different file modes available in Python?

# 'r': Read (default)
# 'w': Write (creates a new file or truncates an existing file)
# 'a': Append (creates a new file or appends to an existing file)
# 'b': Binary mode
# 't': Text mode (default)
# '+': Update mode (read and write)

# 3) How do you read the entire content of a file in Python?
# You can use the read() method to read the entire content of a file.

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# 4) How do you read a file line-by-line in Python?
# You can use the readline() method or iterate over the file object.

with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')

# 5) How do you write to a file in Python?
# You can use the write() method to write to a file.

with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# 6) How do you append to an existing file in Python?
# You can open the file in append mode using 'a' and then use the write() method.

with open('example.txt', 'a') as file:
    file.write('\nAppended text.')

# 7) What is the purpose of the with statement in file handling?
# The with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised. It provides a cleaner and more concise syntax for file handling.

with open('example.txt', 'r') as file:
    content = file.read()

# 8) How do you check if a file exists in Python?
# You can use the os.path.exists() function from the os module.

import os 
if os.path.exists('example.txt'):
    print('File exists')
else:
    print('File does not exist')

# 9) How do you delete a file in Python?
# You can use the os.remove() function from the os module.

import os
os.remove('example.txt')

# 10) How do you rename a file in Python?
# You can use the os.rename() function from the os module.

import os
os.rename('old_name.txt', 'new_name.txt')

# 11)What is the difference between read() and readlines() methods?

# read(): Reads the entire file content as a single string.
# readlines(): Reads the file and returns a list of lines.

# 12)How do you read a binary file in Python?
# You can open the file in binary mode using 'rb'.

with open('example.bin', 'rb') as file:
    content = file.read()

# 13)How do you write to a binary file in Python?
# You can open the file in binary mode using 'wb'.

with open('example.bin', 'wb') as file:
    file.write(b'\x00\xFF')

# 14) How do you move the file pointer to a specific position in a file?
# You can use the seek() method to move the file pointer.

with open('example.txt', 'r') as file:
    file.seek(10)
    content = file.read()

# 15)What is the use of the tell() method in file handling?
# The tell() method returns the current position of the file pointer.

with open('example.txt', 'r') as file:
    print(file.tell())

# 16) do you close a file in Python?
# You can use the close() method to close a file.

file = open('example.txt', 'r')
file.close()

# 16) What is file encoding, and how do you specify it while opening a file?
# File encoding specifies the character encoding used to read/write the file. You can specify it using the encoding parameter.

with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 17) How do you handle exceptions in file handling?
# You can use a try-except block to handle exceptions

try:
    with open('example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File not found')

# 18)What is the difference between text mode and binary mode in file handling?

# Text mode ('t'): The file is read/written as a sequence of characters, with newline characters being translated based on the operating system.

# Binary mode ('b'): The file is read/written as a sequence of bytes, with no translation of newline characters.