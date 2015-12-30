aba = bob = 1
counteething=3
thing = aba+bob
while True:
    if len(str(thing))==1000:
        print counteething
        break
    aba, bob = bob, thing
    thing=aba+bob
    counteething+=1