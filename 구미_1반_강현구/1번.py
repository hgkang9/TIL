import sys
sys.stdin=open('1번.txt','r')

def isposs(y,x):
    if 0<=y<N and 0<=x<N:
        return True

def go(y,x,i):
    mymap[y][x]+=1
    if data[i][2]==0:
        newy=y-data[i][3]
        if isposs(newy,x):
            go(newy,x,i)
    elif data[i][2]==1:
        newy=y+data[i][3]
        if isposs(newy,x):
            go(newy,x,i)
    elif data[i][2]==2:
        newx=x-data[i][3]
        if isposs(y,newx):
            go(y,newx,i)
    else:
        newx=x+data[i][3]
        if isposs(y,newx):
            go(y,newx,i)


T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    data=[list(map(int,input().split())) for i in range(M)]
    mymap=[[0]*N for i in range(N)]
    ans,cnt=0,0

    for i in range(M):
        go(data[i][0],data[i][1],i)

    for y in range(N):
        for x in range(N):
            if mymap[y][x]>ans:
                ans=mymap[y][x]

    for y in range(N):
        for x in range(N):
            if mymap[y][x]==ans:
                cnt+=1

    print('#%d %d %d' %(tc,ans,cnt))
