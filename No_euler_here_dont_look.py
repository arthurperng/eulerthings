from collections import Counter
def replace_ace(hand):
    return [x if x[0]!=1 else (14, x[1]) for x in hand]

def process_card(s):
    suit = s[1]
    number = s[0]
    mapping = {'A':1, 'T':10, 'J':11, 'Q':12, 'K':13}
    if number in mapping:
        n = mapping[number]
    else:
        n=int(number)
    return (n, suit)

def read_file():
    ans = []
    f = open('p054_poker.txt')
    for line in f.readlines():
        cards = map(process_card,line.strip().split(' '))
        ans.append((cards[:5], cards[5:]))
    return ans
def royalflush(g):
    if len(set([x[1] for x in g]))==1 and set([x[0] for x in g]) == set([14, 10, 11, 12, 13]):
        return True
    return False
def straightflush(g):
    thign=set([x[0] for x in g])
    if len(set([x[1] for x in g]))==1 and max(thign)-min(thign)==4:
        return max(thign)
    return False
def fourkind(y):
    c=Counter([a[0] for a in y])
    for i in c:
        if c[i]==4:
            return i
    return 0
def fullhouse(y):
    c=Counter([a[0] for a in y])
    if len(c)==2 and ( c.values()[0]==3 or c.values()[0]==2):
        for i in c:
            if c[i]==3:
                return i
    return 0
def flush(y):
    if len(set([a[1] for a in y]))==1:
        a=[x[0] for x in y]
        a.sort(reverse=True)
        return a
    return []
def straight(z):
    a=set([x[0] for x in z])
    if max(a)-min(a)==4 and len(a)==5:
        return max(a)
    return 0
def threekind(o):
    c=Counter([a[0] for a in o])
    for i in c:
        if c[i]==3:
            return i
    return 0
def twopairs(ok):
    c=Counter([a[0] for a in ok])
    if len(c)==3:
        pairs=[]
        for guy in c:
            if c[guy]==2:
                pairs.append(guy)
            else:
                kicker=guy
        return (max(pairs), min(pairs), kicker)
    return ()
def pair(hihihi):
    c=Counter([a[0] for a in hihihi])
    for i in c:
        if c[i]==2:
            pairhi=i
            kickers=[x for x in c if x!=i]
            kickers.sort(reverse=True)
            return pairhi, kickers
def highcard(hand):
    numbas=[x[0] for x in hand]
    numbas.sort(reverse=True)
    return numbas
    
    
def get_better_pattern(foo, hand14,hand1):
    r= foo(hand14)
    if r:
        return r
    return foo(hand1)
p1win=0   
    
all_games = read_file()
foolist = [royalflush,straightflush,fourkind,fullhouse,flush,straight,threekind,twopairs,pair,highcard]
for handx, handy in all_games:
    handx14 = replace_ace(handx)
    handy14 = replace_ace(handy)
    for foo in foolist:
        royx = get_better_pattern(foo, handx14, handx)
        royy = get_better_pattern(foo, handy14, handy)
        if royx>royy:
            p1win+=1
            break
        elif royx or royy:
            break
print p1win
        
        
