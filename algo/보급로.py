import sys
sys.stdin=open('보급로.txt','r')

dy=[1,0,-1,0]
dx=[0,1,0,-1]
def ispossible(y, x):
    global N
    if y >= 0 and y < N and x >= 0 and x < N:
        if not visited[y][x]:
            return True

def go(y,x):
    global rtime, low, N
    if y==N-1 and x==N-1:
        return
    for dir in range(4):
        newy=y+dy[dir]
        newx=x+dx[dir]
        if ispossible(newy,newx):
            visited[newy][newx]=1
            rtime+=data[newy][newx]
            if rtime>low:
                rtime-=data[newy][newx]
                visited[newy][newx]=0
                return
            go(newy,newx)
            low=rtime
            rtime-=data[newy][newx]
            visited[newy][newx]=0
    if rtime<low:
        low=rtime



T=int(input())
for tc in range(1,T+1):
    N=int(input())
    data=[list(map(int,input())) for _ in range(N)]
    rtime=data[0][0]
    visited=[[0]*N for _ in range(N)]
    visited[0][0]=1
    low=99999999999
    go(0,0)
    print(low)
