"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

HighVal = 999
LowVal = 100

def isPali(Num):
    return str(Num) == str(Num)[::-1]

def LargePali(Bottom, Top):
    PaliCheck = []
    for x in range(Top, Bottom, -1):
        for y in range(Top, Bottom, -1):
            if isPali(x*y):
                PaliCheck.append(x*y)
    return PaliCheck

print(max(LargePali(LowVal,HighVal)))
print(LargePali(LowVal,HighVal))