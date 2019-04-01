import sys
sys.stdin=open('상원생일파티.txt','r')

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    data=[0]*M
    friend=[0]*(N+1)
    s=[0]*(N+1)
    cnt=0
    for i in range(M):
        data[i] = tuple(map(int, input().split()))
    data.sort()
    a=[]
    for i in range(M):
        if data[i][0]==1:
            a.append(data[i][1])
            friend[data[i][1]]=1
        if data[i][1]==1 and friend[data[i][0]]!=1:
            a.append(data[i][0])
            friend[data[i][0]]=1
            friend[data[i][1]]=1
    a.sort()

    for i in range(2,len(friend)):
        if friend[i]:
            cnt+=1

    if cnt>0:
        for i in range(M):
            for j in range(len(a)):
                if data[i][0]!=1 and data[i][1]!=1:
                    if data[i][0]==a[j] and friend[data[i][1]]!=1:
                        friend[data[i][1]]=1
                        cnt+=1
                    elif data[i][1]==a[j] and friend[data[i][0]]!=1:
                        friend[data[i][0]]=1
                        cnt+=1
    print('#%d %d' % (tc, cnt))

