import math

def issquare(D):
    return (math.floor(math.sqrt(D))**2 == D or math.ceil(math.sqrt(D))**2 == D )

def evaluate_continued_fraction(denom):
    frac_num = 0
    frac_denom = 1
    for i in range(len(denom)-1, -1, -1):
        frac_num += denom[i]*frac_denom
        if(i != 0):
            temp = frac_denom
            frac_denom = frac_num
            frac_num = temp

    return frac_num, frac_denom

def construct_continued_fraction(D):
    # compute continued fraction of sqrt(D)
    continued_fraction_coeff = []

    x = math.sqrt(D)
    d = 1
    m = 0
    a0 = math.floor(x)
    continued_fraction_coeff.append(a0)

    a = a0
    while(a != 2*a0):
        m = d*a - m
        d = (D - m*m)/(d)
        a = math.floor((a0 + m)/d)
        continued_fraction_coeff.append(a)

    return continued_fraction_coeff

maxD = 1
maxX = 0

for D in range(1,1001):
    if(not issquare(D)):
        x = 0
        y = 0
        coeff = construct_continued_fraction(D)
        k = len(coeff) - 1
        if(k % 2 == 0):
            coeff.pop()

            x,y = evaluate_continued_fraction(coeff)
        if(k % 2 == 1):
            coeff += coeff[1:k]
            x,y = evaluate_continued_fraction(coeff)
        # print(coeff)
        # print(x,y)
        if(x > maxX):
            maxD = D
            maxX = x

print(maxD)
