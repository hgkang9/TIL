import sys
sys.stdin=open('2048.txt','r')

def pu(data):
    if push=='right':
        for y in range(N):
            for x in range(N-1,0,-1):
                if data[y][x] == 0:
                    data[y][x] = data[y][x-1]
                    data[y][x-1] = 0
    elif push=='left':
        for y in range(N):
            for x in range(N-1):
                if data[y][x] == 0:
                    data[y][x] = data[y][x+1]
                    data[y][x+1] = 0
    elif push=='down':
        for x in range(N):
            for y in range(N-1,0,-1):
                if data[y][x]==0:
                    data[y][x]=data[y-1][x]
                    data[y-1][x]=0
    else:
        for x in range(N):
            for y in range(N-1):
                if data[y][x]==0:
                    data[y][x]=data[y+1][x]
                    data[y+1][x]=0

T=int(input())
for tc in range(1,T+1):
    N,push=map(str, input().split())
    N=int(N)
    data=[list(map(int,input().split())) for i in range(N)]
    check=[[0]*N for i in range(N)]
    if push=='right':
        for i in range(N):
            pu(data)
        for y in range(N):
            for x in range(N-1,0,-1):
                if data[y][x]==data[y][x-1] and not check[y][x]:
                    data[y][x]*=2
                    data[y][x-1]=0
                    check[y][x]=1
        for i in range(N):
            pu(data)

    elif push=='left':
        for i in range(N):
            pu(data)
        for y in range(N):
            for x in range(N-1):
                if data[y][x]==data[y][x+1] and not check[y][x]:
                    data[y][x]*=2
                    data[y][x+1]=0
                    check[y][x]=1
        for i in range(N):
            pu(data)

    elif push=='down':
        for i in range(N):
            pu(data)
        for x in range(N):
            for y in range(N-1,0,-1):
                if data[y][x]==data[y-1][x] and not check[y][x]:
                    data[y][x]*=2
                    data[y-1][x]=0
                    check[y][x]=1
        for i in range(N):
            pu(data)

    else:
        for i in range(N):
            pu(data)
        for x in range(N):
            for y in range(N-1):
                if data[y][x] == data[y+1][x] and not check[y][x]:
                    data[y][x]*=2
                    data[y+1][x] = 0
                    check[y][x] = 1
        for i in range(N):
            pu(data)

    print('#%d' %tc)
    for y in range(N):
        print(*data[y])


