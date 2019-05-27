import math
import random
from math import sqrt; from itertools import count, islice

# def operationOnHash(hashmap):

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


if __name__ == '__main__':

    hash =  {}

    for i in range(100):
        hash[i] = random.randint(1, 10000)

    rezultat = list(map(lambda x : (x if (x % 2 == 0) else x+1), hash.values()))

    primes = list(filter(lambda x : x if(isPrime(x)) else None, hash.values()))


    print(primes)

    print(hash)

    print(rezultat)
