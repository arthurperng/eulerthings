def binaryplain(g):
    return g==int(str(g)[::-1]) and int(bin(g)[2:])==int(bin(g)[2:][::-1])
print sum([i for i in range(1,1000000) if binaryplain(i)])

