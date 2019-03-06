import sys
sys.stdin=open('파스칼.txt', 'r')

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    data=[[0 for _ in range(N)] for _ in range(N)]
    data[0][0] = 1

    for y in range(1,N):
        for x in range(N):
            data[y][0] = 1
            data[y][y] = 1

    for y in range(1,N):
        for x in range(1,N-1):
            data[y][x] = data[y-1][x-1] + data[y-1][x]

    print('#%d' % tc)
    for y in range(N):
        for x in range(N):
            if data[y][x]:
                print(data[y][x], end=' ')
        print('')

