# Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313.
# We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).
#
# There are 120 reversible numbers below one-thousand.
#
# How many reversible numbers are there below one-billion (109)?

import time

start = time.time()

def isReversible(n):
    if(n % 10 == 0):
        return False

    n_str = str(n)

    reverse = n_str[::-1]

    if(int(reverse) % 2 == n % 2):
        return False

    for c in (str(int(reverse)+n)):
        if (int(c) % 2 == 0):
            return False
    return True

numReversible = 0
for i in range(1, 10**8):
    if isReversible(i):
        numReversible += 1

end = time.time()
print("time taken: " + str(end - start))
print(numReversible)
