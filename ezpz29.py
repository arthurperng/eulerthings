asdf=set()
for a in range(2, 101):
    for b in range(2, 101):
        number=a**b
        asdf.add(number)
print len(asdf)