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
