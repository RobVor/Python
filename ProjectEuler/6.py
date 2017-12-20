"""The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

Naturals = [i for i in range(1,101)]

def SumSqr(Num):
    SumSqrt = 0
    for i in Num:
        SumSqrt += i**2
    return SumSqrt

def SqrOfSum(Num):
    SqrtOfSum = 0
    for i in Num:
        SqrtOfSum += i
    SqrtOfSum = SqrtOfSum**2
    return SqrtOfSum

Final = SqrOfSum(Naturals) - SumSqr(Naturals)
print(Final)