#!python
# -*- coding: utf-8 -*-
""" This program was created to quickly split URL links lists. The URL links are placed in a file called "Links.txt" and the program should then be executed.
Once executed the program will try and create 8 equal length list files (1 - 8.txt) with an equal amount of records for download. The last file might be a record or so short
based on whether the Links.txt file record count can be evenly split between 8 files or not. The application reads the file, and pops off the last record into the new file(s) 
until all records have been split between them. This can then be used with the bulk image downloader in multiple instances to actually do the downloads.
Copyright 2017 - 2018, ROBERT VORSTER ALL RIGHTS RESERVED
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Robert Vorster <rob.vor@gmail.com>, December 2017
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.
"""

__author__ = "Robert Vorster"
__contact__ = "rob.vor@gmail.com"
__copyright__ = "Copyright 2018 - 2019, ROBERT VORSTER ALL RIGHTS RESERVED"
__date__ = "2017/01/06"
__deprecated__ = False
__email__ =  "rob.vor@gmail.com"
__maintainer__ = "Robert Vorster"
__status__ = "Production"
__version__ = "0.1.0"

fileCount = 8
with open("Links.csv", "r") as fileFeed:
    fileFeed.seek(0)
    content = fileFeed.readlines()
    
if len(content) > 8:
    records = int(len(content) / 8) + 1
    for file in range(1, fileCount + 1):
        linesOut = []
        with open(str(file) + ".txt", "w") as Output:
            for line in range(records):
                if len(content) > 0:
                    linesOut.append(content.pop())
            Output.writelines(linesOut)
