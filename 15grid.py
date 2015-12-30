from operator import *
def factorial(number):
    return reduce(mul, range(1, number+1))
print factorial(40)/(factorial(20)*factorial(20))