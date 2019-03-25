import sys
sys.stdin=open('종이의개수.txt','r')

def calc(y,x,size):
    for i in range(y,y+size):
        for j in range(x,x+size):
            if data[y][x]!=data[i][j]:
                return False
    return True

def start(y,x,size):
    if calc(y,x,size):
        cnt[data[y][x]+1]+=1
        return
    next=size//3
    for i in range(3):
        for j in range(3):
            start(y+i*next, x+j*next, next)

N=int(input())
data=[list(map(int,input().split())) for _ in range(N)]
cnt=[0]*3
start(0,0,N)
for i in cnt:
    print(i)
