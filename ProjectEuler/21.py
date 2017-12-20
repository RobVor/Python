"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

import time

startTime = time.time()
print("Started: " + str(startTime))

def SumDivisors(int):
    result = 0
    for i in range(1,int):
        if int%i == 0:
            result += i
    return result

def AmicablePairs(intFrom, intTo):
    Div = [SumDivisors(i) for i in range(intFrom, intTo + 1)]
    pairs = []
    for i in range(intTo - intFrom + 1):
        pos = Div[i]
        if i + intFrom < pos and intFrom <= pos and pos <= intTo and Div[pos - intFrom] == i + intFrom:
            pairs.append([i + intFrom, pos])
    return pairs

def SumPairs(pairs):
    result = 0
    for pair in pairs:
        result += sum(pair)
    return result

FinalResult = SumPairs(AmicablePairs(1,10000))
print(FinalResult)
endTime = time.time()
print("Ended: " + str(endTime))
Secs = endTime - startTime
print("Took: " + str(Secs))