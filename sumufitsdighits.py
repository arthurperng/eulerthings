def suum(number):
    return sum([int(y)**5 for y in str(number)])==number
total=0
for guy in range(10, 1000000):
    if suum(guy):
        total+=guy
print total


