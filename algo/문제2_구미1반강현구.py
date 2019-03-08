import sys
sys.stdin=open('문제2.txt','r')
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    height=0
    count=0

    for y in range(N):
        for x in range(N):
            if data[y][x]>height:
                height=data[y][x]

    for y in range(N):
        for x in range(N):
            if (data[y][x] and data[y+1][x]==0 and y+1<N and data[y+1][x-1]!=0) or (data[y][x] and y==N-1):
                if (data[y][x+1] == 0 and x+1<N) or (data[y][x] and x==N-1):
                    count+=1

    print('#%d %d %d' %(tc, count, height))