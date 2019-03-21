import sys
sys.stdin=open('화물도크.txt','r')
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    data=[0]*N
    count=1
    for i in range(N):
        data[i]=tuple(map(int,input().split()))
    data.sort(key=lambda x:x[1])
    t=data[0][1]
    for i in range(1,N):
        if data[i][0]>=t:
            count+=1
            t=data[i][1]
    print('#{} {}' .format(tc,count))