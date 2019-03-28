import sys
sys.stdin=open('그룹나누기.txt','r')

def findset(x):
    if x==p[x]:
        return x
    else:
        return findset(p[x])
def union(x,y):
    p[findset(y)]=findset(x)

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    data1=list(map(int,input().split()))
    data=[0]*M
    p=[0]*(N+1)
    for i in range(M):
        if data1[i*2]>data1[i*2+1]:
            data[i]=(data1[i*2+1],data1[i*2])
        else:
            data[i]=(data1[i*2],data1[i*2+1])

    for i in range(N+1):
        p[i]=i

    for i in range(len(data)):
        union(data[i][0],data[i][1])

    for i in range(1, N + 1):
        p[i]=findset(p[i])

    cnt=0
    checker=[0]*(N+1)
    for i in range(1,N+1):
        if checker[p[i]]!=1:
            checker[p[i]]=1
            cnt+=1

    print('#%d %d' %(tc, cnt))