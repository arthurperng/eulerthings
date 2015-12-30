from math import *
primelist=[]
def primeornot(number):
    for butt in primelist:
        if number%butt==0 and butt<ceil(sqrt(number))+1:
            return False
    return True
total=2
for i in range(3, 2000001, 2-):
    if primeornot(i):
        total+=i
        primelist.append(i)
        print i
print total