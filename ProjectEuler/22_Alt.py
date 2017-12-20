"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""

import time

startTime = time.time()
print("Started: " + str(startTime))

with open('names.txt', 'r') as file:
    y = sorted([x.strip('"') for x in file.read().split(',')])
print(sum([a * b for a, b in zip([sum([ord(l) - ord('A') + 1 for l in c]) for c in y], range(1, len(y) + 1))]))

endTime = time.time()
print("Ended: " + str(endTime))
Secs = endTime - startTime
print("Took: " + str(Secs))