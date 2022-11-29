import random
import itertools

# random namning
from typing import List, Any, Union


def RandRemove(LIST):
    x = random.randint(0, (len(LIST) - 1))
    y = LIST[x]
    LIST.remove(y)
    return (y, LIST)


def Generate(h, u, y, t, r):
    llst = []
    while len(h) + len(u) + len(y) + len(t) + len(r) > 5:
        (yh, l1) = RandRemove(h)
        (yu, l2) = RandRemove(u)
        (yy, l3) = RandRemove(y)
        (yt, l4) = RandRemove(t)
        (yr, l5) = RandRemove(r)
        h = l1
        u = l2
        y = l3
        t = l4
        r = l5
        if len(l1) + len(l2) + len(l3) + len(l4) + len(l5) < 5:
            break
        msg = '{}{}{}{}{}'.format(yh, yu, yy, yt, yr)
        # j=len(l1) + len(l2) + len(l3) + len(l4) + len(l5)
        llst.append(msg)

    return llst


Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

'''clones of Alphabet'''
a = Alphabet[:]
b = Alphabet[:]
c = Alphabet[:]
d = Alphabet[:]
e = Alphabet[:]

'''prin = (Generate(a, b, c, d, e))
print(len(prin))'''


# noinspection SpellCheckingInspection
def generate2(h, u, y, t, r):
    #     for e
    msseg = []
    (yh, l1) = RandRemove(h)
    (yu, l2) = RandRemove(u)
    (yy, l3) = RandRemove(y)
    (yt, l4) = RandRemove(t)
    mseg = f'{yh}{yu}{yy}{yt}'
    while len(r) != 0:
        (yr, l5) = RandRemove(r)
        mseeg = mseg + yr
        msseg.append(mseeg)

    #     for a
    mssag = []
    (yh, l1) = RandRemove(h)
    (yu, l2) = RandRemove(u)
    (yy, l3) = RandRemove(y)
    (yt, l4) = RandRemove(t)
    msag = f'{yh}{yu}{yy}{yt}'
    while len(r) != 0:
        (yr, l5) = RandRemove(r)
        msaag = msag + yr
        mssag.append(msaag)

        # for b
    mssbg = []
    (yh, l1) = RandRemove(h)
    (yu, l2) = RandRemove(u)
    (yy, l3) = RandRemove(y)
    (yt, l4) = RandRemove(t)
    msbg = f'{yh}{yu}{yy}{yt}'
    while len(r) != 0:
        (yr, l5) = RandRemove(r)
        msbbg = msbg + yr
        mssbg.append(msbbg)

    #     for c
    msscg = []
    (yh, l1) = RandRemove(h)
    (yu, l2) = RandRemove(u)
    (yy, l3) = RandRemove(y)
    (yt, l4) = RandRemove(t)
    mscg = f'{yh}{yu}{yy}{yt}'
    while len(r) != 0:
        (yr, l5) = RandRemove(r)
        msccg = mscg + yr
        msscg.append(msccg)

    #     for d
    mssdg = []
    (yh, l1) = RandRemove(h)
    (yu, l2) = RandRemove(u)
    (yy, l3) = RandRemove(y)
    (yt, l4) = RandRemove(t)
    msdg = f'{yh}{yu}{yy}{yt}'
    while len(r) != 0:
        (yr, l5) = RandRemove(r)
        msddg = msdg + yr
        mssdg.append(msddg)
    return (mssag + mssbg + msscg + mssdg + msseg)


# mssg = []
# msssg = 'ghgh'
# while True:
#     (yr, l5) = RandRemove(e)
#     msssg += yr
#     mssg.append(msssg)
#     print(mssg)

print((generate2(a, b, c, d, e)))

#
# def permutations(iterable, r=None):
#     # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
#     # permutations(range(3)) --> 012 021 102 120 201 210
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     if r > n:
#         return
#     indices = list(range(n))
#     cycles = list(range(n, n - r, -1))
#     yield tuple(pool[i] for i in indices[:r])
#     while n:
#         for i in reversed(range(r)):
#             cycles[i] -= 1
#             if cycles[i] == 0:
#                 indices[i:] = indices[i + 1:] + indices[i:i + 1]
#                 cycles[i] = n - i
#             else:
#                 j = cycles[i]
#                 indices[i], indices[-j] = indices[-j], indices[i]
#                 yield tuple(pool[i] for i in indices[:r])
#                 break
#         else:
#             return
#
#
# def permutationss(iterable, r=None):
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     for indices in product(range(n), repeat=r):
#         if len(set(indices)) == r:
#             yield tuple(pool[i] for i in indices)


print(itertools.permutations(Alphabet, 2))
