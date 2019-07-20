# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
#
# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#
# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#
# Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy.
# In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
#
# Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
#
# Find the least number for which the proportion of bouncy numbers is exactly 99%.

def isbouncy(num):
    numstring = str(num)
    bouncy = False
    greater = 2
    for i in range(len(numstring)-1):
        if (numstring[i] > numstring[i+1]):
            if(greater == 0):
                bouncy = True
            greater = 1
        if (numstring[i] < numstring[i+1]):
            if(greater == 1):
                bouncy = True
            greater = 0

    return bouncy

numBouncy = 0
bouncy = []
total = 2000000
for i in range(1, total):

    if (isbouncy(i)):
        numBouncy += 1
    if(99*i == numBouncy *100):
        print(numBouncy, i)
