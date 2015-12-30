p=[200, 100, 50, 20, 10, 5, 2, 1]
def coins(amount, coin):
    ways=0
    if p[coin]==1 or amount==0:
        return 1
    for bim in range((amount/p[coin])+1):
        difamount=amount-bim*p[coin]
        ways+=coins(difamount, coin+1)
    return ways
print coins(200, 0)

