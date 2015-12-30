from math import *
def divisors(number):
    things=0
    for hi in range(1, int(sqrt(number))+1):
        if number%hi==0:
            if number/hi==hi:
                things+=hi
            elif hi==1:
                things+=1
            else:
                if hi==1:
                    things+=1
                things+=number/hi
                things+=hi
    return things
total=0
for cable in range(1, 10001):
    notcable=divisors(cable)
    if divisors(notcable)==cable and notcable>cable:
        if notcable>10000:
            total+=cable
        else:
            total+=notcable
            total+=cable
print total
