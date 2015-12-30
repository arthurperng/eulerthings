biggest=1
bignumber=0
def collatzlen(number, count):
    if number==1:
        return count
    elif number%2==0:
        count+=1
        return collatzlen(number/2, count)

    else:
        count+=1
        return collatzlen(3*number+1, count)
for number in range(1, 1000000):
    length=collatzlen(number, 1)
    if length>biggest:
        biggest=length
        bignumber=number
        print number
print bignumber
print biggest


