"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

import math

Seq = []
QMax = 600851475143
def Prime(Num):
    div = 2
    while div < Num:
        if Num%div == 0 and Num/div > 1:
            Num /= div
            div = 2
        else:
            div += 1
    return int(Num)

print(Prime(QMax))