import random

Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def RandRemove(LIST):
    llst = []
    while len(LIST) > 0:
        x = random.randint(0, (len(LIST) - 1))
        y = LIST[x]
        LIST.remove(y)
        return (y, LIST)

'''a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
d = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
e = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
'''

'''def generate(l1, l2, l3, l4, l5):
    empty=[]
    while len(l1) + len(l2) + len(l3) + len(l4) + len(l5) >=5:
        (x, l1)=RandRemove(l1)
        (yy, l2)=RandRemove(l2)
        (z, l3)=RandRemove(l3)
        (q, l4)=RandRemove(l4)
        (w, l5)=RandRemove(l5)
        msg='{}{}{}{}{}'.format(x, yy, z, q, w)
        empty.append(msg)
    return empty

print(generate(a, b, c, d, e))
'''


def gen2(xx, yyy, zz, qq, ww):
    smth = '{}{}{}{}{}'.format(xx, yyy, zz, qq, ww)
    return smth


while len(a) > 0 and len(b) > 0 and len(c) > 0 and len(d) > 0 and len(e) > 0:
    (x, a) = RandRemove(a)
    (yy, b) = RandRemove(b)
    (z, c) = RandRemove(c)
    (q, d) = RandRemove(d)
    (w, e) = RandRemove(e)
    print(gen2(x, yy, z, q, w))
    print(len(a), len(b), len(c), len(d), len(e))

