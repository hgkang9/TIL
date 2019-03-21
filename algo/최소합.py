import sys
sys.stdin=open('최소합.txt','r')

dy=[1,0]
dx=[0,1]

def isposs(y,x):
    global N
    if y >= 0 and y < N and x >= 0 and x < N:
        return True

def go(y,x):
    global sum,low
    if y==N-1 and x==N-1:
        if sum<low:
            low=sum
        return
    if sum>low:
        return
    for dir in range(2):
        newy=y+dy[dir]
        newx=x+dx[dir]
        if isposs(newy,newx):
            sum += data[newy][newx]
            go(newy,newx)
            sum-=data[newy][newx]

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    data=[[0]*N for _ in range(N)]
    for i in range(N):
        data[i]=list(map(int,input().split()))
    sum=data[0][0]
    low=100000000
    go(0,0)
    print('#{} {}' .format(tc,low))