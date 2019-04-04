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
    low1=99999
    ans1=99999
    ans2=0
    a=[]
    for y in range(N):
        for x in range(N):
            low=0
            go(y,x)
            if low>=ans2:
                ans2=low
                # a.append(data[y][x])
            else:
                break

    print(visited)
    # for y in range(N):
    #     for x in range(N):

    # for i in range(len(a)):
    #     if a[i][1]==low:
    #         if low1>a[i][0]:
    #             ans1=a[i][0]
    # ans1=min(a)
    print(a)
    print(tc, ans1, ans2)