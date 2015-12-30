def gcfplease(cherry, notacherry):
    a, b=max(cherry, notacherry), min(cherry, notacherry)
    if a%b==0:
        return b
    else:
        return gcfplease(b, a%b)
def common(a, b):
    gcf=gcfplease(a, b)
    return a/gcf, b/gcf
n=1
d=1
for e in range(1, 10):
    for f in range(e, 10):
        for g in range(e+1, 10):
            if common(10*e+f, 10*f+g)==common(e, g):
                print 10*e+f
                print 10*f+g
                n*=e
                d*=g
print common(n, d)
