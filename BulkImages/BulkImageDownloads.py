#!python
# -*- coding: utf-8 -*-
""" This program was created to quickly download bulk images from URL links. The URL links are placed in a file called "Links.txt" and the program should then be executed.

Copyright 2017 - 2018, ROBERT VORSTER ALL RIGHTS RESERVED
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Robert Vorster <rob.vor@gmail.com>, December 2017

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Robert Vorster"
__contact__ = "rob.vor@gmail.com"
__copyright__ = "Copyright 2017 - 2018, ROBERT VORSTER ALL RIGHTS RESERVED"
__date__ = "2017/12/31"
__deprecated__ = False
__email__ =  "rob.vor@gmail.com"
__maintainer__ = "Robert Vorster"
__status__ = "Production"
__version__ = "0.0.1"

import re, os, urllib.request

with open("Links.txt","r") as src:
    src.seek(0)
    Links = src.readlines()
print("We have found {} links to process...".format(len(Links)))

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

for link in Links:
    link = link.replace("\n","")
    filename = os.path.basename(link).split("?")[0]
    try:
        urllib.request.urlretrieve(link,filename)
    except:
        print("The following links where rejected or produced an error, even though we changed the user agent to allow downloading.")
        print(link)
