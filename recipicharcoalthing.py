def refeating(boing):
    gong=1
    numbas=[]
    while True:
        gong*=10
        dong=gong%boing
        if dong in numbas:
            return len(numbas)
        elif dong==0:
            return 0
        numbas.append(dong)
grrrn=0
gahhl=0
print refeating(7)
for blegh in range(1, 1001):
    genth=refeating(blegh)
    if genth>gahhl:
        grrrn=blegh
        gahhl=genth
    print genth, grrrn
print grrrn

