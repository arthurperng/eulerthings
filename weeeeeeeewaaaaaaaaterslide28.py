up = 0
smallestnumber = 1
total = 1
for loop in range(1, 501):
    smallestnumber+=up*4+2
    up+=2
    print 'smallestnumber=', smallestnumber
    total += smallestnumber*4+up*6
    print "total=", total
print total
