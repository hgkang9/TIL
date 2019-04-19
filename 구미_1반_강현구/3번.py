import sys
sys.stdin=open('3번.txt','r')

def go(depth,summ):
    global ans
    if depth==N:
        if summ==L:
            ans=1
        return

    if summ>L:
        return

    if summ==L:
        ans=1
        return

    visited[depth]=1
    go(depth+1,summ+data[depth])
    visited[depth]=0
    go(depth+1,summ)

T=int(input())
for tc in range(1,T+1):
    N,L=map(int,input().split())
    data=list(map(int,input().split()))
    visited=[0]*N
    ans=0
    go(0,0)
    print('#%d %d' %(tc,ans))
