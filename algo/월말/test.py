import sys
sys.stdin=open('test.txt','r')

# dy=[3,2,-2,-3,-3,-2,2,3]
# dx=[2,3,3,2,-2,-3,-3,-2]
#
# def isposs(y,x):
#     if 0<=y<N and 0<=x<N and not visited[y][x]:
#         return True
#
# def go(y,x,cnt):
#     global low
#     if y==data[2] and x==data[3]:
#         if cnt<low:
#             low=cnt
#             return
#     if cnt>low:
#         return
#     for i in range(8):
#         newy=y+dy[i]
#         newx=x+dx[i]
#         if isposs(newy,newx):
#             visited[newy][newx]=1
#             go(newy,newx,cnt+1)
#             visited[newy][newx]=0
#
# T=int(input())
# for tc in range(1,T+1):
#     N=int(input())
#     data=list(map(int, input().split()))
#     visited=[[0]*N for i in range(N)]
#     cnt=0
#     low=9999999
#     go(data[0],data[1],cnt)
#     print(low)

# def calc(a,b,c):
#     global cs
#     cs=0
#     cs=abs(a-b)+abs(b-c)+abs(c-a)
#     return cs
#
# def mysum(y1,y2,x1,x2):
#     global summ
#     summ=0
#     for y in range(y1,y2):
#         for x in range(x1,x2):
#             summ+=data[y][x]
#     return summ
#
# T=int(input())
# for tc in range(1,T+1):
#     N,M=map(int,input().split())
#     data=[list(map(int,input().split())) for i in range(N)]
#     cs, summ,low=0,0,0
#     for y in range(1,N):
#         for x1 in range(1,M-1):
#             for x2 in range(x1+1,M):
#                 A=mysum(0,y,0,x1)
#                 B=mysum(0,y,x1,x2)
#                 C=mysum(0,y,x2,M)
#                 D=mysum(y,N,0,x1)
#                 E=mysum(y,N,x1,x2)
#                 F=mysum(y,N,x2,M)
#                 li=[[A,B,C],[A,B,D],[A,B,E],[A,B,F],[A,C,D],[A,C,E],[A,C,F],[A,D,E],[A,D,F],[A,E,F],
#                     [B,C,D],[B,C,E],[B,C,F],[B,D,E],[B,D,F],[B,E,F],
#                     [C,D,E],[C,D,F],[C,E,F],[D,E,F]]
#                 for i in range(len(li)):
#                     calc(li[i][0], li[i][1], li[i][2])
#                     if cs>low:
#                         low=cs
#     print(low)

def go(depth,d):
    global low
    if depth==N:
        if d<low:
            low=d
        return
    if d>low:
        return

    for x in range(N):
        if not visited[x]:
            visited[x]=1
            go(depth+1,d+data[depth][x])
            visited[x]=0

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    snack=list(map(int,input().split()))
    robot=list(map(int,input().split()))
    sn=[0]*N
    ro=[0]*N
    low=9999999
    for i in range(N):
        sn[i]=[snack[i*2],snack[i*2+1]]
        ro[i]=[robot[i*2],robot[i*2+1]]

    data=[[0]*N for i in range(N)]
    for y in range(N):
        for x in range(N):
            data[y][x]=abs(ro[y][0]-sn[x][0])+abs(ro[y][1]-sn[x][1])
    visited=[0]*N

    go(0,0)
    print(low)