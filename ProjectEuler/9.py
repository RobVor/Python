"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2."""

def Pythagorean_Triplet(N):
    for a in range(1,N):
        for b in range(1,N):
            c = 1000 - a - b
            if c > 0:
                if c*c==a*a+b*b:
                    print(a*b*c)
                    break

Pythagorean_Triplet(1000)