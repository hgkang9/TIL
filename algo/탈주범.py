import sys, time
stime = time.time()
sys.stdin=open('탈주범.txt','r')

dy=[1,0,-1,0]
dx=[0,1,0,-1]
def isposs(y,x):
    if 0<=y<N and 0<=x<M:
        if not visited[y][x]:
            return True
def go(y,x,L):
    global cnt
    que.append((y,x))
    visited[y][x]=1
    while que:
        y,x=que.pop(0)
        if visited[y][x]==L:
            return
        for i in range(4):
            newy=y+dy[i]
            newx=x+dx[i]
            if i ==0 and (mymap[y][x]==1 or mymap[y][x]==2 or mymap[y][x]==5 or mymap[y][x]==6):
                if isposs(newy,newx) and (mymap[newy][newx]==1 or mymap[newy][newx]==2 or mymap[newy][newx]==4 or mymap[newy][newx]==7):
                    visited[newy][newx]=visited[y][x]+1
                    que.append((newy,newx))
                    cnt+=1
            elif i ==1 and (mymap[y][x]==1 or mymap[y][x]==3 or mymap[y][x]==4 or mymap[y][x]==5):
                if isposs(newy,newx) and (mymap[newy][newx]==1 or mymap[newy][newx]==3 or mymap[newy][newx]==6 or mymap[newy][newx]==7):
                    visited[newy][newx] = visited[y][x] + 1
                    que.append((newy,newx))
                    cnt+=1
            elif i ==2 and (mymap[y][x]==1 or mymap[y][x]==2 or mymap[y][x]==4 or mymap[y][x]==7):
                if isposs(newy,newx) and (mymap[newy][newx]==1 or mymap[newy][newx]==2 or mymap[newy][newx]==5 or mymap[newy][newx]==6):
                    visited[newy][newx] = visited[y][x] + 1
                    que.append((newy,newx))
                    cnt+=1
            elif i==3 and (mymap[y][x]==1 or mymap[y][x]==3 or mymap[y][x]==6 or mymap[y][x]==7):
                if isposs(newy,newx) and (mymap[newy][newx]==1 or mymap[newy][newx]==3 or mymap[newy][newx]==4 or mymap[newy][newx]==5):
                    visited[newy][newx] = visited[y][x] + 1
                    que.append((newy,newx))
                    cnt+=1

T=int(input())
for tc in range(1,T+1):
    N,M,R,C,L=map(int,input().split())
    mymap=[list(map(int,input().split())) for _ in range(N)]
    que=[]
    visited=[[0]*M for i in range(N)]
    cnt=1
    go(R,C,L)
    print('#%d %d' %(tc,cnt))
    print(time.time()-stime)