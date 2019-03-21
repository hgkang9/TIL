import sys
sys.stdin=open('전기카트.txt','r')

def go(res,y):
    global sum, low
    for i in range(len(res)+1):
        if i==len(res):
            sum+=data[y][0]
        else:
            sum+=data[y][res[i]]
            y=res[i]
    if sum<low:
        low=sum

def getsome(depth):
    global N, low, sum
    if depth==(N-1):
        sum=0
        go(res,0)
        return
    for i in range((N-1)):
        if not visited[i]:
            visited[i]=True
            res[depth]=i+1
            getsome(depth+1)
            visited[i]=False

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    data=[list(map(int,input().split())) for _ in range(N)]
    visited=[0]*(N-1)
    res=[0]*(N-1)
    sum = 0
    low = 999999999999999
    getsome(0)
    print('#%d %d' %(tc,low))