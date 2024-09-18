x, y = map(int, input().split())
xs, ys = map(int, input().split())
M = int(input())

if (xs == 0 and ys == 0) or (xs == x and ys == y) or (xs == 0 and ys == y) or (xs == x and ys == 0):
    ubinkosong = 3
elif xs == 0 or ys == 0 or xs == x or ys == y:
    ubinkosong = 5
else:
    ubinkosong = 8

if M == 0:
    ubinkosong = 0
elif M == 1:
    x1, y1 = map(int, input().split())
elif M == 2:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
elif M == 3:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    if (xs+1 == x1 or xs-1 == x1) or (ys+1 == y1 or ys-1 == y1):
        ubinkosong -= 1
    if (xs+1 == x2 or xs-1 == x2) or (ys+1 == y2 or ys-1 == y2):
        ubinkosong -= 1
    if (xs+1 == x3 or xs-1 == x3) or (ys+1 == y3 or ys-1 == y3):
        ubinkosong -= 1
elif M == 4:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    if (xs+1 == x1 or xs-1 == x1) or (ys+1 == y1 or ys-1 == y1):
        ubinkosong -= 1
    if (xs+1 == x2 or xs-1 == x2) or (ys+1 == y2 or ys-1 == y2):
        ubinkosong -= 1
    if (xs+1 == x3 or xs-1 == x3) or (ys+1 == y3 or ys-1 == y3):
        ubinkosong -= 1
    if (xs+1 == x4 or xs-1 == x4) or (ys+1 == y4 or ys-1 == y4):
        ubinkosong -= 1
elif M == 5:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    x5, y5 = map(int, input().split())
    if (xs+1 == x1 or xs-1 == x1) or (ys+1 == y1 or ys-1 == y1):
        ubinkosong -= 1
    if (xs+1 == x2 or xs-1 == x2) or (ys+1 == y2 or ys-1 == y2):
        ubinkosong -= 1
    if (xs+1 == x3 or xs-1 == x3) or (ys+1 == y3 or ys-1 == y3):
        ubinkosong -= 1
    if (xs+1 == x4 or xs-1 == x4) or (ys+1 == y4 or ys-1 == y4):
        ubinkosong -= 1
    if (xs+1 == x5 or xs-1 == x5) or (ys+1 == y5 or ys-1 == y5):
        ubinkosong -= 1
elif M == 6:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    x5, y5 = map(int, input().split())
    x6, y6 = map(int, input().split())
    if (xs+1 == x1 or xs-1 == x1) or (ys+1 == y1 or ys-1 == y1):
        ubinkosong -= 1
    if (xs+1 == x2 or xs-1 == x2) or (ys+1 == y2 or ys-1 == y2):
        ubinkosong -= 1
    if (xs+1 == x3 or xs-1 == x3) or (ys+1 == y3 or ys-1 == y3):
        ubinkosong -= 1
    if (xs+1 == x4 or xs-1 == x4) or (ys+1 == y4 or ys-1 == y4):
        ubinkosong -= 1
    if (xs+1 == x5 or xs-1 == x5) or (ys+1 == y5 or ys-1 == y5):
        ubinkosong -= 1
    if (xs+1 == x6 or xs-1 == x6) or (ys+1 == y6 or ys-1 == y6):
        ubinkosong -= 1
elif M == 7:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    x5, y5 = map(int, input().split())
    x6, y6 = map(int, input().split())
    x7, y7 = map(int, input().split())
    if (xs+1 == x1 or xs-1 == x1) or (ys+1 == y1 or ys-1 == y1):
        ubinkosong -= 1
    if (xs+1 == x2 or xs-1 == x2) or (ys+1 == y2 or ys-1 == y2):
        ubinkosong -= 1
    if (xs+1 == x3 or xs-1 == x3) or (ys+1 == y3 or ys-1 == y3):
        ubinkosong -= 1
    if (xs+1 == x4 or xs-1 == x4) or (ys+1 == y4 or ys-1 == y4):
        ubinkosong -= 1
    if (xs+1 == x5 or xs-1 == x5) or (ys+1 == y5 or ys-1 == y5):
        ubinkosong -= 1
    if (xs+1 == x6 or xs-1 == x6) or (ys+1 == y6 or ys-1 == y6):
        ubinkosong -= 1
    if (xs+1 == x7 or xs-1 == x7) or (ys+1 == y7 or ys-1 == y7):
        ubinkosong -= 1
elif M == 8:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    x5, y5 = map(int, input().split())
    x6, y6 = map(int, input().split())
    x7, y7 = map(int, input().split())
    x8, y8 = map(int, input().split())
    if (xs+1 == x1 or xs-1 == x1) or (ys+1 == y1 or ys-1 == y1):
        ubinkosong -= 1
    if (xs+1 == x2 or xs-1 == x2) or (ys+1 == y2 or ys-1 == y2):
        ubinkosong -= 1
    if (xs+1 == x3 or xs-1 == x3) or (ys+1 == y3 or ys-1 == y3):
        ubinkosong -= 1
    if (xs+1 == x4 or xs-1 == x4) or (ys+1 == y4 or ys-1 == y4):
        ubinkosong -= 1
    if (xs+1 == x5 or xs-1 == x5) or (ys+1 == y5 or ys-1 == y5):
        ubinkosong -= 1
    if (xs+1 == x6 or xs-1 == x6) or (ys+1 == y6 or ys-1 == y6):
        ubinkosong -= 1
    if (xs+1 == x7 or xs-1 == x7) or (ys+1 == y7 or ys-1 == y7):
        ubinkosong -= 1
    if (xs+1 == x8 or xs-1 == x8) or (ys+1 == y8 or ys-1 == y8):
        ubinkosong -= 1


if ubinkosong > 0:
    print("Senshi makan hari ini!")
else:
    print("Senshi makannya besok aja deh.")