# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
#
# 1! + 4! + 5! = 1 + 24 + 120 = 145
#
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
#
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
#
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
#
# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)
#
# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
#
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?


factorials = [1,1,2,6,24,120,720,5040,40320,362880]
def computeFact(n):
  sum = 0
  while(n > 0):
    sum += factorials[n % 10]
    n = n//10
  return sum

dp= [0]*(10**7+5)
dp[169] = 3
dp[363601] = 3
dp[1454] = 3
dp[871] = 2
dp[872] = 2
dp[45361] = 2
dp[45362] = 2

total = 0
for i in range(5, 10**6):
  num = 0
  current = i
  while (dp[current] == 0):
    newcurrent = computeFact(current)
    num += 1
    if(newcurrent == current):
      break
    current = newcurrent

  dp[i] = num + dp[current]

for i in range(len(dp)):
  if (dp[i] == 60):
    total += 1

print(total)
