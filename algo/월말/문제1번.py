from collections import deque
import sys
sys.stdin=open('문제1.txt','r')

def isposs(y,x):
    if y>=0 and y<N and x>=0 and x<N:
        if not visited[y][x]:
            return True

dy=[3,3,2,-2,-3,-3,-2,2]
dx=[-2,2,3,3,2,-2,-3,-3]

# cost_map=[]
# for i in range(0,N):
#     line=[0]*N
#     cost_map.append(line)
#
def go(starty,startx,endy,endx):
    global low, cnt
    if starty==endy and startx==endx:
        if cnt<low:
            low=cnt
        return
    if cnt>low:
        return
    cnt += 1
    for i in range(8):
        newy=starty+dy[i]
        newx=startx+dx[i]

        if isposs(newy,newx):
            # if(data[newy][newx]<cnt)
            que.append((newy,newx,cnt))
            visited[newy][newx] = 1

    a=que.popleft()
    cnt=a[2]

    go(a[0],a[1],endy,endx)
    visited[newy][newx] = 0
    cnt-=1

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    data=list(map(int,input().split()))
    low=999999
    cnt=0
    visited=[[0]*N for _ in range(N)]
    que=deque()
    go(data[0],data[1],data[2],data[3])
    # go(3,2,4,7)
    print('#%d %d' %(tc,low))

