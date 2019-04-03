import sys
sys.stdin=open('최대상금.txt','r')

def change(data):
    global ma,ma_i
    if not data:
        return
    ma = max(data)
    ma_i = 0
    for i in range(len(data)):
        if data[ma_i]<=data[i]:
            ma=data[i]
            ma_i=i
    if ma_i!=0:
        data[ma_i],data[0]=data[0],data[ma_i]
    else:
        a.append(data.pop(0))
        change(data)

T=int(input())
for tc in range(1,T+1):
    num,N=map(int,input().split())
    data=list(map(int,str(num)))
    cnt=1
    visited=[0]*len(data)
    ma = max(data)
    ma_i = 0
    a=[]
    change(data)
    while cnt!=N:
        if data:
            a.append(data.pop(0))
            change(data)
            cnt+=1

    print(a+data)