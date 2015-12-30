def chair(listylist):
    if len(listylist)==1:
        return [listylist]
    tatale=[]
    for ant in listylist:
        listlisty=[dat for dat in listylist if dat!=ant]
        guy=chair(listlisty)
        guy=[[ant]+dat for dat in guy]
        tatale+=guy
    return tatale
deloares = chair([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print deloares[999999]

