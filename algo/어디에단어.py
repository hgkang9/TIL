import sys
sys.stdin=open('어디에단어.txt','r')
T=int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    data=[[0 for _ in range(N)] for _ in range(N)]
    clone=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    count=0
    ans=0
    for y in range(N):
        count=0
        for x in range(N):
            if data[y][x]:
                count+=1
            if not data[y][x]:
                count=0
            if count==K:
                if x+1>=N:
                    ans+=1
                    pass
                if x+1<N:
                    if not data[y][x+1]:
                        ans+=1

    for y in range(N):
        for x in range(N):
            clone[y][x]=data[x][y]

    for y in range(N):
        count=0
        for x in range(N):
            if clone[y][x]:
                count+=1
            if not clone[y][x]:
                count=0
            if count==K:
                if x+1>=N:
                    ans+=1
                    pass
                if x+1<N:
                    if not clone[y][x+1]:
                        ans+=1
    print('#{} {}' .format(tc, ans))