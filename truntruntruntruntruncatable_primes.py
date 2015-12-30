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
    while bound <= math.sqrt(number)+1:
        if primeornot(bound):
            primelist.append(bound)
            if number%bound==0:
                return False

        bound+=1
    return True
def trumpcatable(number):
    if number<10:
        return False
    if not primeornot(number):
        return False
    for i in range(1,len(str(number))):
        if not primeornot(int(str(number)[i:])):
            return False
    for i in range(1, len(str(number))):
        if not primeornot(int(str(number)[:i])):
            return False
    return True

print primeornot(25)

total=0
count=0
number=10
while count<11:
    if trumpcatable(number):
        print number
        total+=number
        count+=1
    number+=1
print total

