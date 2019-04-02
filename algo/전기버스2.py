import sys
sys.stdin=open('전기버스2.txt','r')

def go(p):
    global cnt, low, N
    if cnt>low:
        return
    if p==N:
        if cnt-1<low:
            low=cnt-1
            return
    for i in range(data[p],0,-1):
        if p+i<=N:
            cnt+=1
            go(p+i)
            cnt-=1

T=int(input())
for tc in range(1,T+1):
    data=list(map(int,input().split()))+[999]
    N=data[0]
    p=1
    cnt=0
    low=99999999

    go(p)
    print('#%d %d' %(tc,low))


