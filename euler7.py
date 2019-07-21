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

i = 3
while(len(primes) != 10001):
    if is_prime(i):
        primes.append(i)
    i += 1

print(primes[-1])
