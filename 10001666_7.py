num=2
import math
primelist=[]
from math import *
def primeornot(number):
    for butt in primelist:
         if butt<math.sqrt(number)+1:
            if number%butt==0:
                return False
         else:
            break
    return True
while len(primelist)<10001:
    if primeornot(num):
        primelist.append(num)
    num+=1
num-=1
print primelist
print num