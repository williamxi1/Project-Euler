# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
import math

primes = [2]

def is_prime(n):
    for prime in primes:
        if(prime < math.floor(n**0.5)+2):
            if(n % prime) == 0:
                return False
        else:
            break
    return True

big_number = 1000000
for i in range(3, big_number):
    if is_prime(i):
        primes.append(i)

maxlen = 0
bestprime = 0
for i in range(len(primes)):
    tot = 0
    for j in range(i , len(primes)):
        tot += primes[j]
        if(tot > 1000000):
            break
        if(is_prime(tot)):
            if(j - i + 1 > maxlen):
                maxlen = j-i + 1
                bestprime = tot

print(bestprime)
