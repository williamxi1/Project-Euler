# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math
num = 600851475143

def computePrimeFactors(n):
    primefactors = []
    for i in range(2, math.floor(n**0.5)+3):
        div = i
        power = 0
        while(n % i == 0):
            power += 1
            n = n/i
        if(power > 0):
            primefactors.append((div, power))
    return primefactors

numfactors = computePrimeFactors(num)
print(numfactors[-1][0])
