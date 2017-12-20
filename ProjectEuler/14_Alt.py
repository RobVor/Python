import time


def collatz(chain_dict, number):
    chain = 0
    n = number
    while n > 1:
        if n < number:
            chain += chain_dict[n]
            chain_dict[number] = chain
            return chain_dict
        if n % 2 == 0:
            n /= 2
            chain += 1
        else:
            n = 3 * n + 1
            chain += 1
    chain_dict[number] = chain
    return chain_dict


def maxCollatz(number):
    chain_dict = {}
    maxchain = 0
    for i in range(1, number + 1):
        chain_dict = collatz(chain_dict, i)
        chain = chain_dict[i]
        if chain > maxchain:
            maxchain = chain
            answer = i
    return answer


Start_time = time.time()
print(maxCollatz(1000000))
print(time.time() - Start_time)