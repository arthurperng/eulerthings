sos=0
sqos=0
for something in range(101):
    sqos+=something*something
for hi in range(101):
    sos+=hi
sos=sos*sos
print sos-sqos