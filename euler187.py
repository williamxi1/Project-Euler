import math
import bisect

def SieveOfEratosthenes(n):

    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    primes = []
    for i in range(2, n+1):
        if(prime[i] == 1):
            primes.append(i)
    return primes


primes = SieveOfEratosthenes(50000000)
print(primes[-1])
print("DONE")

answer = 0
for prime in primes:
    if(prime > 10000):
        break
    else:
        answer += bisect.bisect(primes, 10**8//prime) + 1

print(answer)
