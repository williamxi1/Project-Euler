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

for i in range(3,7500):
    if(is_prime(i)):
        primes.append(i)


ans = 0
expressibleNumbers = {}

for i in primes:
    print(i)
    for j in primes[0:300]:
        for k in primes[0:80]:
            num = i**2 + j**3 + k**4
            if (num <= 50000000):
                if(num not in expressibleNumbers):
                    expressibleNumbers[num] = 1
                    ans += 1
print(ans)
