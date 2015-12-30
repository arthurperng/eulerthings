total = 0

for book in range(1, 1000):
    if book%3==0:
        total+=book
    elif book%5==0:
        total+=book
print total