"""n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""

ToTheN = 100

def SumOfDigits(nth):
    Track = nth
    result = 0
    for i in range(nth-1, 0, -1):
        Track *= i
    SumOf = str(Track)
    for j in SumOf:
        result += int(j)
    return result

print(SumOfDigits(ToTheN))