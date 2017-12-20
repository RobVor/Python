"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

MaxQ = 10001

def PrimeToTheN(Nth):
    prime_list = [2]
    num = 3
    while len(prime_list) < Nth:
        for p in prime_list:
            if num%p == 0:
                break
        else:
            prime_list.append(num)
        num += 2
    return prime_list

print(max(PrimeToTheN(MaxQ)))