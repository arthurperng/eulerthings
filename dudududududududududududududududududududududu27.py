import math
primelist=[2]
bound = 3
from math import *
def primeornot(number):
    global bound
    if number < bound:
        return number in primelist
    for butt in primelist:
         if butt<math.sqrt(number)+1:
            if number%butt==0:
                return False
         else:
            break
    while bound < math.sqrt(number):
        if primeornot(bound):
            primelist.append(bound)
            if number%bound==0:
                return False

        bound+=1
    return True
def abn(a, b, n):
    return (n*n)+(a*n)+b



big = 0
bigl = 0
for a in range(-1000, 1001):
    print a
    for b in range(-1000, 1001):
        #print b
        n=0
        count = 0
        while primeornot(abn(a, b, n)):
            count+=1
            if count>bigl:
                big=a*b
                bigl=count
            n+=1


print big





