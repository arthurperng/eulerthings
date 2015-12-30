number=[1]

for grrr in range(1000):
    c=0
    for jk in range(len(number)):
        number[jk]*=2
        r=number[jk]%10+c
        c=number[jk]/10
        number[jk]=r


    if c>0:
        number.append(c)
print sum(number)




