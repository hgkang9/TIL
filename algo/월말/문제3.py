import sys
sys.stdin=open('문제3.txt','r')

#로봇 하나가 과자 하나를 먹을 때 이동거리
def calc(ry,rx,sy,sx):
    global cs
    cs=0
    cs=abs(ry-sy)+abs(rx-sx)
    return cs

def go(rob,res):
    global low
    if rob==N:
        if res<low:
            low=res
        return
    if res>low:
        return
    for sna in range(N):
        if not visited[sna]:
            visited[sna]=True
            go(rob+1, res+distance[rob][sna])
            visited[sna]=False

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    snack=list(map(int,input().split()))
    robot=list(map(int,input().split()))
    cs=0
    sn=[0]*N
    ro=[0]*N
    for i in range(N):
        sn[i] = [snack[i*2], snack[i*2+1]]
        ro[i] = [robot[i*2], robot[i*2+1]]

    distance=[[0]*N for i in range(N)]
    for r in range(N):
        for s in range(N):
            distance[r][s] = calc(ro[r][0], ro[r][1], sn[s][0],sn[s][1])

    visited=[0]*N
    low=9999999999

    go(0,0)
    print('#%d %d' %(tc,low))