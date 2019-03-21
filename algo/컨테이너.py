import sys
sys.stdin=open('컨테이너.txt','r')
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    co=list(map(int,input().split()))
    tr=list(map(int,input().split()))
    co_check=[0]*N
    tr_check=[0]*M
    co.sort()
    co.reverse()
    tr.sort()
    tr.reverse()
    ans=0
    for i in range(N):
        for j in range(M):
            if tr[j]>=co[i] and tr_check[j]==0 and co_check[i]==0:
                ans+=co[i]
                co_check[i]=1
                tr_check[j]=1
    print('#%d %d'%(tc,ans))