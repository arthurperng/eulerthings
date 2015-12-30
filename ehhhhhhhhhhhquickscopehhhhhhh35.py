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
def circular(gah):
    a=str(gah)
    if "2" in a or "4" in a or "5" in a or "6" in a or "8" in a or "0" in a:
        return False
    for green in range(len(a)):
        if not primeornot(int(a)):
            return False
        a=a[1:] + a[0]
    return True
count=0
for i in range(2, 1000000):
    if circular(i):
        print i
        count+=1
print count+1




