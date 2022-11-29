

'''def next(list, start=0):
    i = len(list)
    j = 0
    while True:
        if j == 0:
            j += 1
            return 0
        elif j + 1 == i:
            j = 0
            return i - 1
        elif j < i:
            j += 1
            return j - 1
        elif j > i:
            break
    return (print('j > i'))

ol = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

while True:
    i = len(ol)
    j = 0
    if j == 0:
        j += 1
        print (0)
    elif j + 1 == i:
        j = 0
        print (i - 1)
    elif j < i:
        j += 1
        print (j - 1)
    elif j > i:
        print('j > i')
'''
import asyncio

async def main():
    await asyncio.sleep(0)
    return 42
print(main())