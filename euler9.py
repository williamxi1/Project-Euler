# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for i in range(1,500):
    for j in range(i,500):
        k = 1000- i - j
        if(i**2 + j**2 == k**2):
            print(i*j*k)
