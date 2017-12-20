file = open("example.txt", 'r')
print(type(file))
content = file.read()
print(content)
content = file.readlines()
print(content)
file.seek(0)
content = file.readlines()
print(content)
contentNew = [i.rstrip("\n") for i in content]
print(contentNew)

file.close()

with open("Writer.txt", 'a+') as file:
    file.write("And another line gets added!")


"""
File 'Open' methods:

r   - Open for reading.
r+  - Open for reading and writing. File pointer (seek) is placed at the start of the file and writes move content down. (Newest first)
w   - Open for writing.
w+  - Open for writing and reading. File will be overwritten. If the file does not exist, will be created.
a   - Open for appending. File pointer (seek) is placed at the end of the file and new content will be added to the bottom of the file. (Oldest first) If the file does not exist, creates it.
a+  - Open for appending and reading. File pointer (seek) is set to the end of the file. New content gets added to the bottom of the file. If the file does not exist, creates it.

Using of 'With'

Including the 'With' statement in file operations will close the file ant the end of the file operations without requiring the .close() method.
"""