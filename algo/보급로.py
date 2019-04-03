import sys
sys.stdin=open('보급로.txt','r')

dy=[1,0,-1,0]
dx=[0,1,0,-1]
def ispossible(y, x): return True if 0<=y<N and 0<=x< N else False
def go(y,x):
    que.append((y,x))
    visited[y][x] = 1
    while que:
        y,x=que.pop(0)
        for i in range(4):
            newy=y+dy[i]
            newx=x+dx[i]
            if ispossible(newy,newx) and not visited[newy][newx]:
                visited[newy][newx] = visited[y][x]+data[newy][newx]
                que.append((newy,newx))
            elif ispossible(newy,newx) and visited[newy][newx] > visited[y][x]+data[newy][newx]:
                visited[newy][newx] = visited[y][x]+data[newy][newx]
                que.append((newy, newx))

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    data=[list(map(int,input())) for _ in range(N)]
    visited=[[0]*N for _ in range(N)]
    que=[]
    go(0,0)
    print(visited[-1][-1]-1)
