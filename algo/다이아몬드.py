import sys
sys.stdin = open("다이아.txt", "r")

TC=int(input())
for tc in range(1, TC+1):
    N=list(map(str,input()))
    l=len(N)
    w=3*l+l+1
    data=[[0 for _ in range(w)] for _ in range(5)]

    for i in range(w):
        data[0][i] = '.'
        data[4][i] = '.'
        if i % 4 == 2:
            data[0][i] = '#'
            data[4][i] = '#'

    for i in range(w):
        if i % 2:
            data[1][i] = '#'
            data[3][i] = '#'
        else:
            data[1][i] = '.'
            data[3][i] = '.'

    for i in range(w):
        if i % 4 == 2:
            data[2][i] = N.pop(0)
        elif i % 4 == 0:
            data[2][i] = '#'
        else:
            data[2][i] = '.'

    for y in range(5):
        for x in range(w):
            print(data[y][x], end='')
        print('')
