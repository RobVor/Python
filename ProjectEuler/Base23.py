import math

def get_proper_divisors(x):
    if x == 1:
        return set()

    small_divisors = set([i for i in range(1,int(math.sqrt(x))+1) if x%i==0])
    big_divisors = set([int(x / i) for i in small_divisors if i!=1])
    return small_divisors | big_divisors

def is_abundand(x):
    return sum(get_proper_divisors(x)) > x

def is_sum_of_two_abundant(x):
    for i in range(2, int(x/2)+1):
        if is_abundand(i) and is_abundand(x-i):
            return True
    else:
        return False

if __name__ == '__main__':
    print(sum([i for i in range(1,28124) if not is_sum_of_two_abundant(i)]))