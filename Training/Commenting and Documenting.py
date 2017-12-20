import os

"""This block will create a doc stream for capturing documentation on while coding. Once done, the doc stream can be obtained by importing the module and calling the appropriate .__doc__ command eith on the import or on classes and function definitions"""

# Get all of the files in the current directory
All_Files = os.listdir()

#For each of the files...
for f in All_Files:
    with open(f,'r') as File:
        print("\n" + "***" + f + "***" + "\n")
        File.seek(0)
        content = File.readlines()
        content = [c.rstrip("\n") for c in content]
        for l in content:
            print(l)