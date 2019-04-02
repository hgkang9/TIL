import sys
sys.stdin=open('동철일분배.txt','r')

def calc(depth):
    global N,sum,low
    if depth==N:
        if sum>low:
            low=sum
        return
    if low>=sum:
        return
    for i in range(N):
        if not visited[i]:
            if data[depth][i]==0:
                continue
            else:
                sum*=(data[depth][i]/100)
                visited[i]=True
                calc(depth+1)
                sum*=(100/data[depth][i])
                visited[i] = False

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    data=[list(map(int,input().split())) for i in range(N)]
    visited=[0]*N
    sum=1
    low=0
    calc(0)
    ans=low*100
    print('#%d' %tc, end=' ')
    print('%0.6f' %ans)