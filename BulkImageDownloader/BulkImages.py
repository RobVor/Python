#!python
# -*- coding: utf-8 -*-
""" This program was created to quickly download bulk images from URL links. The URL links are placed in a file called "Links.txt" and the program should then be executed.

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
__copyright__ = "Copyright 2017 - 2018, ROBERT VORSTER ALL RIGHTS RESERVED"
__date__ = "2017/12/31"
__deprecated__ = False
__email__ =  "rob.vor@gmail.com"
__maintainer__ = "Robert Vorster"
__status__ = "Production"
__version__ = "0.0.6"

import pathlib, sys, re, os, urllib.request
cwd = os.path.dirname(os.path.abspath(__file__))
sourceFile = os.path.dirname(sys.executable) + "\Links.txt"

with open(sourceFile,"r") as src:
    src.seek(0)
    Links = src.readlines()
print("We have found {} links to process...".format(len(Links)))

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

Limit = 0

for link in Links:
    Limit += 1
    link = link.replace("\n","")
    filename = os.path.basename(link).split("?")[0]
    filename = os.path.dirname(sys.executable) + "/" + filename
    fileExists = pathlib.Path(filename)
    if Limit == 1000:
        sys.exit()
    try:
        if fileExists.is_file():
            print("File exists, skipping file, downloading next...")
            with open(sourceFile, "r+") as fileUpdate:
                OldFile = fileUpdate.readlines()
                fileUpdate.seek(0)
                for item in OldFile:
                    if item != str(link)+"\n":
                        fileUpdate.write(item)
                fileUpdate.truncate()
            pass
        else:
            urllib.request.urlretrieve(link,filename)
            with open(sourceFile, "r+") as fileUpdate:
                OldFile = fileUpdate.readlines()
                fileUpdate.seek(0)
                for item in OldFile:
                    if item != str(link)+"\n":
                        fileUpdate.write(item)
                fileUpdate.truncate()
    except:
        print("The following links where rejected or produced an error, even though we changed the user agent to allow downloading.")
        print(link)
        with open("Error_Links.txt", "a") as errFile:
            errFile.write(str(link)+"\n")
print("All links have been processed.")
