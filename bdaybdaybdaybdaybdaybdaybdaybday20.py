number=[1]

import sys

c=0
for bookybook in range(1, 101):
    for jk in range(len(number)):
        number[jk]*=bookybook
        number[jk]+=c
        r=(number[jk])%10
        c=(number[jk])/10
        number[jk]=r
    while c>0:
        number.append(c%10)
        c=c/10
    print number
print sum(number)

