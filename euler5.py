# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def gcd(a,b):
    if(b == 0):
        return a
    return gcd(b, a%b)

ans = 1
for i in range(1,21):
    ans *= (i//gcd(i, ans))

print(ans)
