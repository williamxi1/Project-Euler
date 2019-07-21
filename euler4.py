# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    return str(n) == str(n)[::-1]

bestans = 0
for i in range(100,1000):
    for j in range(100,1000):
        ans = i*j
        if(ans > bestans and is_palindrome(ans)):
            bestans = ans
print(bestans)
