import sys
sys.stdin=open('이상한나라.txt','r')

def Steal(nowy,nowx,dir,jump):

    dx = [0, 0, -jump, jump]
    dy = [-jump, jump, 0, 0]

    nexty=nowy+dy[dir]
    nextx=nowx+dx[dir]

    if IsSafe(nexty,nextx):
        Mymap[nexty][nextx]+=1
        Steal(nexty,nextx,dir,jump)

def IsSafe(y,x):
    if x>=0 and x<N and y>=0 and y<N:
        return True
    else:
        return False


TC=int(input())
for tc in range(1,TC+1):
    print("#%d"%tc,end=' ')
    N,M=map(int,input().split())
    Rabbit=[0]*M
    for m in range(M):
        Rabbit[m]=list(map(int,input().split()))

    Mymap = [[0] * N for _ in range(N)]
    dx=[0,0,-1,1] #dir:0~3
    dy=[-1,1,0,0]

    for r in range(M):
        ry=Rabbit[r][0]
        rx=Rabbit[r][1]
        dir=Rabbit[r][2]
        jump=Rabbit[r][3]
        Mymap[ry][rx]+=1
        Steal(ry,rx,dir,jump)

    mymax=-1
    for y in range(N):
        tmp=max(Mymap[y])
        if mymax<tmp:
            mymax=tmp

    print(mymax,end=' ')
    cnt=0
    for y in range(N):
        for x in range(N):
            if Mymap[y][x]==mymax:
                cnt+=1
    print(cnt)

