f=[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
def digitorial(a):
    return a == sum([f[int(x)] for x in str(a)])
print sum([x for x in range(10,2000001) if digitorial(x)])

total=0
for b in range(10, 2000001):
    if digitorial(b):
        print b
        total+=b
print total



