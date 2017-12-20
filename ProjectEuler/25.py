"""The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""

import time

startTime = time.time()
print("Started: " + str(startTime))

MaxQ = 10000

def FiboSeq(Counter):
    Start = [1,1]
    for i in range(Counter):
        Start.append(Start[-1] + Start[-2])
        if len(str(Start[i])) == 1000:
            return Start.index(i)

for i in range(MaxQ):
    Result = FiboSeq(i)
print(Result)

endTime = time.time()
print("Ended: " + str(endTime))
Secs = endTime - startTime
print("Took: " + str(Secs))