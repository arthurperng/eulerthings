a=[[0]*21]*21
for y in range(0, 22):
    for x in range(0, 22):
        if x==0 or y==0:
            a[y][x]=1
        else:
            a[y][x]=a[y-1][x]+a[y][x-1]
print a[20][20]
