"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""

import time

startTime = time.time()
print("Started: " + str(startTime))

namesList = []

with open("names.txt", "r") as InputFile:
    InputFile.seek(0)
    Content = InputFile.read()
    print(Content)
    for name in Content.split(","):
        namesList.append(name.lstrip('"').rstrip('"'))

namesList.sort()

letterScore = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
letterScore2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def NameScores(names):
    namedScores = {}
    result = 0
    for n in names:
        score = 0
        for c in n:
            #score += letterScore[c]                #Using a dictionary from above
            #score += 1 + letterScore2.index(c)     #Using a list from above
            score += ord(c) - 64                    #Using ordinal character position
        namedScores[n] = score * (1+names.index(n))
    for i in namedScores.values():
        result += i
    print(namedScores["COLIN"])
    return result

print(NameScores(namesList))

endTime = time.time()
print("Ended: " + str(endTime))
Secs = endTime - startTime
print("Took: " + str(Secs))