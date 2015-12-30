import sys
biggest=0
for dave in range(999, 100, -1):
    for buster in range(999, 100, -1):
        if dave>=buster:
            testnumber=dave*buster
            stringthing=str(testnumber)
            if stringthing==stringthing[::-1]:
                biggest=max(biggest, testnumber)

print biggest