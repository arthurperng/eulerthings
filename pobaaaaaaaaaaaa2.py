a = b = 1
thing = a+b
toytal = 0
while thing<4000000:
    if thing%2==0:
        toytal += thing
    a, b = b, thing
    thing=a+b


print toytal
