import sys
sys.stdin=open('정사각형방.txt','r')

dy=[1,0,-1,0]
dx=[0,1,0,-1]

def isposs(y,x):
    if 0<=y<N and 0<=x<N:
        return True

def go(y,x):
    global low
    que.append((y,x))
    visited[y][x]=1
    low=0
    while que:
        y,x=que.pop(0)
        for i in range(4):
            newy = y + dy[i]
            newx = x + dx[i]
            if isposs(newy,newx) and data[newy][newx]-data[y][x]==1:
                visited[newy][newx]=visited[y][x]+1
                que.append((newy,newx))
    for y in range(N):
        for x in range(N):
            if visited[y][x]>low:
                low=visited[y][x]

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    data=[list(map(int,input().split())) for i in range(N)]
    visited=[[0]*N for i in range(N)]
    que=[]
    low1=0
    low2=0
    ans1=0
    ans2=0
    for y in range(N):
        for x in range(N):
            go(y,x)
            if low>ans2:
                ans1=data[y][x]
                if ans1<data[y][x]:
                    ans1=data[y][x]
                ans2=low
            else:
                break
    print(tc, ans1,ans2)