def read_file():
    ans = []
    f = open('p054_poker.txt')
    for line in f.readlines():
        cards = line.strip().split(' ')
        ans.append(cards)
    return ans

print read_file()[0]
