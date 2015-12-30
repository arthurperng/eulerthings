def pandigital(number):
    digits=set([x for x in number])
    if not "0" in number and len(digits)==9:
        return True
    return False
biggest=0
for n in range(1,10000):
    print n
    c=""
    for multiply in range(1, 10):
        d=n*multiply
        c+=str(d)
        if len(c)==9 and pandigital(c):
            print n, multiply, c
            biggest=max(int(c), biggest)
            break
        if len(c)>9:
            break
print biggest









