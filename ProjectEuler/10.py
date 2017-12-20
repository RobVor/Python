"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

MaxQ = 2000000
Product = 0

def SumOfPrime(Num):
    s = list(range(Num + 1))
    s[1] = 0
    sqrtn = int(round(Num ** 0.5))
    for i in range(2, sqrtn + 1):
        s[i * i: Num + 1: i] = [0] * len(range(i * i, Num + 1, i))
    return filter(None, s)

for i in list(SumOfPrime(MaxQ)):
    Product += i

print(Product)