"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

Seq = [x for x in range(1,20+1)]
Steps = 20

def GetDiv(Step):
    Div = []
    for i in range(Step,999999999,Step):
        if all(i % n == 0 for n in Seq):
            print(i)
            break
    return None

GetDiv(Steps)