from math import *
trianglenumber=1
countup=2
def divisors(number):
    things=0
    for hi in range(1, int(sqrt(number))+1):
        if number%hi==0:
            if number/hi==hi:
                things+=1
            else:
                things+=2
    return things
while True:
    if divisors(trianglenumber)>500:
        print trianglenumber
        break
    trianglenumber+=countup
    countup+=1




