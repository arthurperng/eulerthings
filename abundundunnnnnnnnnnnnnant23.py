from math import *
def abundundant(number):
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
    return things>number
total=0
all_abundant_numbers = [i for i in range(12,28123) if abundundant(i)]
for dingdong in range(1, 28123):
    for dongding in all_abundant_numbers:
        if dongding>dingdong/2:
            print dingdong
            total+=dingdong
            break
        if (dingdong-dongding) in all_abundant_numbers:
            break
print total

