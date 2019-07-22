# In the context of formal languages, any finite sequence of letters of a given alphabet Σ is called a word over Σ. We call a word incomplete if it does not contain every letter of Σ.
#
# For example, using the alphabet Σ={a,b,c}, 'ab', 'abab' and '' (the empty word) are incomplete words over Σ, while 'abac' is a complete word over Σ.
#
# Given an alphabet Σ of α letters, we define I(α,n) to be the number of incomplete words over Σ with a length not exceeding n.
# For example, I(3,0)=1, I(3,2)=13 and I(3,4)=79.
#
# Find I(107,1012). Give your answer modulo 1000000007.



MOD = 10**9 + 7

final_alpha = 10**7
final_length = 10**12

factorials = [0] * (10**7+5)
factorials[0] = 1
factorials[1] = 1
for i in range(2,len(factorials)):
  factorials[i] = (factorials[i-1] * i) % MOD


def modular_pow(base, exponent):

    result = 1
    base = base % MOD
    while (exponent > 0):
        if (exponent % 2):
           result = result * base % MOD
        exponent = exponent//2
        base = (base * base) % MOD
    return result

def inverse(n):
  u = n
  v = MOD
  x1 = 1
  x2 = 0
  while(u != 1):
    q = v//u
    r = v- q*u
    x = x2 - q*x1
    v = u
    u = r
    x2 = x1
    x1 = x
  return x1%MOD

def binom(top, bottom):
  return ( (factorials[top] * inverse(factorials[bottom]) % MOD) * (inverse(factorials[top - bottom])) ) % MOD

def terms(index):
  # terms in alpha
  if(final_alpha - index == 1):
    return (( final_alpha +MOD )*( final_length + 1) * (-1)** (index+1) + MOD) % MOD - MOD
  elif (final_alpha - index == 0):
    return (-1)** (index + 1) %MOD

  else:
    return (-1)** (index + 1)  * (modular_pow(final_alpha - index, final_length+1) - 1) * (inverse( final_alpha - index -1) %MOD) * (binom(final_alpha, final_alpha - index) %MOD)

ans = 0
for i in range(1, final_alpha+1):
  if(i%100000 == 0):
      print(i)
  ans = (ans + terms(i)) % MOD

print(ans)
