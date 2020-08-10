from numpy import zeros
from random import *

a = zeros((3, 3), int)

b = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
for i in range(7):
    t = choice(b)
    row1 = b.index(t)

    coloum1 = choice(t)
    del b[row1][coloum1]
    a[row1][coloum1] = 1

    print(a)
    print('')
    print("NOW IT'S YOUR TURN!!!")
    print('YOUR MARK IS 2')

    row = int(input("ENTER THE ROW:"))
    coloum = int(input('ENTER THE COLOUM:'))

    while (row == row1 and row == coloum1):
        print(f'The entered combination of values {row, coloum} is been already used ')
        row = int(input("ENTER THE ROW:"))
        coloum = int(input("ENTER THE COLOUM:"))
    a[row][coloum] = 2
    c = b[row][coloum]
    for I in range(2):
        for J in range(2):
            if b[I][J] == b[row][coloum]:
                del b[I][J]
    print("----------")
    print(b)
    print('----------')

    print(a)
    print("NEXT \n ROUND")
    r = 0
    c = 0
    c1 = 0
    r1 = 0
    s = 0
    s = 0
    s = 0
    d = 0

    w = 0
    q = 0
    l = 0
    k = 0
    if (r == 0 and c == 0) or (r1 == 0 and c1 == 0):
        while r <= 2 and r1 <= 2:
            e = [s, k, w, l, d, q]

            s = 0
            d = 0
            w = 0
            q = 0
            l = 0
            K = 0
            for m in range(2):
                s = a[r][m] + s
                d = a[r1][m] + d
                w = a[m][c] + w
                q = a[m][c1] + q
                l = a[m][m] + l
                k = a[m][2 - m] + k
            if s == 6:
                print('you won')
                break

            elif d == 3:
                print('you lose')
                break
            elif l == 3:
                print('you lose')
                break
            elif l == 6:
                print('you win')
                break
            elif k == 3:
                print('you lose')
                break
            elif k == 6:
                print('you win')
                break

            elif q == 3:
                print('you lose')
                break
            elif w == 6:
                print('you win')
                break
            else:
                print('no result')
                break

            r += 1
            r1 += 1
            c += 1
            c1 += 1
