import sys
sys.stdin=open('색종이','r')

def IsSafe(y,x,size):
    for i in range(size):
        for j in range(size):
            if y+i<10 and x+j<10:
                if data[y+i][x+j]!=1:
                    return False
            else:
                return False
    return True

def change(y,x,size,point):
    for i in range(size):
        for j in range(size):
            if point==-1:
                data[y+i][x+j]=-1
            else:
                data[y+i][x+j]=1

def paper():
    global cnt,low,color
    if not color:
        if low>cnt:
            low=cnt
        return

    if cnt>low:
        return

    y=x=-1
    for i in range(10):
        for j in range(10):
            if data[i][j]==1:
                y=i
                x=j
                break
        if y>=0:
            break

    for p in range(5,0,-1):
        if cp[p] and IsSafe(y,x,p):
            cnt+=1
            color-=p*p
            cp[p]-=1
            change(y,x,p,-1)
            paper()
            cp[p]+=1
            cnt-=1
            color+=p*p
            change(y,x,p,1)


cp=[0,5,5,5,5,5]
data=[]
for i in range(10):
    data.append(list(map(int,input().split())))

color=0
for y in range(10):
    for x in range(10):
        if data[y][x]==1:
            color+=1

cnt=0
low=26
paper()
if low==26:
    print(-1)
else:
    print(low)
