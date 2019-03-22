import sys
sys.stdin=open('최적경로.txt','r')

def dist(a,b):
    global D
    D=abs(a[0]-b[0])+abs(a[1]-b[1])
    return D

def go(res,s):
    global D,N,low
    for i in range(N):
        D+=dist(data[s],data[res[i]])
        s=res[i]
        if D>low:
            return
    D+=dist(data[s],data[1])
    if D<low:
        low=D

def getsome(depth):
    global N, low, D
    if depth==N:
        D=0
        go(res,0)
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            res[depth]=data2[i]
            getsome(depth+1)
            visited[i]=False

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    data1=list(map(int,input().split()))
    data2=[0]*N
    data=[]
    D=0
    low=9999999999
    for i in range(len(data1)-1):
        if not i%2:
            data.append((data1[i],data1[i+1]))
    visited = [0] * N
    res = [0] * N
    for i in range(2,N+2):
        data2[i-2]=i

    getsome(0)

    print('#%d %d' %(tc,low))
