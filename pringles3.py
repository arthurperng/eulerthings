from math import *
def primeornot(number):
    for butt in range(2, int(ceil(sqrt(number)))):
        if number%butt==0:
            return False
    return True


for buttons in range(int(sqrt(600851475143)+1), 1, -1):
    if 600851475143%buttons==0 and int(primeornot(buttons)):
        print buttons
        break
