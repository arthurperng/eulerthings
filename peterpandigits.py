def peterpan(number, numberber):
    product=number*numberber
    number, numberber, product=str(number), str(numberber), str(product)
    baa=number+numberber+product
    digits=set([int(x) for x in baa])
    if 0 in digits:
        return 0
    elif len(digits)==9 and len(baa)==9:
        print number, numberber, product
        return int(product)
    else:
        return 0
h=set()
for i in range(2, 100):
    for j in range(100, 50001):
        h.add(peterpan(i, j))
print sum(h)





