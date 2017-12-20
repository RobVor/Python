import json, difflib

"""Use difflib to find matches of words and terms

difflib.SequenceMatcher(None, "rainn", "rain").ration()
 - This will return a match probability as a percentage between 0 and 1. In this case 0.8888

 - To compare values in a list or dictionary, like the JSON file used here, use:
 
 difflib.get_close_matches(word/list, how many matches?, cutoff= %ration)
"""

data = json.load(open("data.json", 'r'))

def GetWordDef(word):
    if word.lower() in data:
        print("The word '%s' means: " % word)
        for defs in data[word]:
            print("-",defs)
    elif word.capitalize() in data:
        print("The word '%s' means: " % word.capitalize())
        for defs in data[word.capitalize()]:
            print("-", defs)
    elif len(difflib.get_close_matches(word,data, n = 1,cutoff= 0.8)) > 0:
        answer = input("Did you mean %s? Enter 'Y' if yes, or 'N' if no: " % difflib.get_close_matches(word,data, n = 1,cutoff= 0.8)[0]).upper()
        if answer == "Y":
            print("The word '%s' means: " % str(difflib.get_close_matches(word, data, n=1, cutoff=0.8)[0]))
            for re_defs in data[difflib.get_close_matches(word,data, n = 1,cutoff= 0.8)[0]]:
                print("-",re_defs)
        else:
            print("The word you typed does not exist. Please try again.")
    else:
        print("The word you typed does not exist. Please try again.")


Word = input("Enter a word you want a definition for: ")
GetWordDef(Word)