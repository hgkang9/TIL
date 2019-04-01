import sys
sys.stdin=open('문제3.txt','r')

#로봇 하나가 과자 하나를 먹을 때 이동거리
def calc(ry,rx,sy,sx):
    global cs
    cs=0
    cs=abs(ry-sy)+abs(rx-sx)
    return cs

def per(depth):
    if depth==N:
        #()
        print(res)
        return
    for i in range(N):
        if not visited:
            visited[i]=True
            res[i]=data[depth]
            per(depth+1)
            visited[i]=False

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    snack=list(map(int,input().split()))
    robot=list(map(int,input().split()))
    cs=0
    visited=[0]*N
    res=[0]*N
    data=[0]*N
    for i in range(1,N+1):
        data[i-1]=i
    per(0)
