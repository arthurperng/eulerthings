def gcfplease(cherry, notacherry):
    a, b=max(cherry, notacherry), min(cherry, notacherry)
    if a%b==0:
        return b
    else:
        return gcfplease(b, a%b)
def lcmok(thing1, thing2):
    return (thing1*thing2)/gcfplease(thing1, thing2)
number=1

for bouncyball in range(1, 21):
   number=lcmok(bouncyball, number)
print number




