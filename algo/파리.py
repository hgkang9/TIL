import sys
sys.stdin=open('파리.txt','r')
T=int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    data=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    ans=0

    for y in range(1, N):
        for x in range(1, N):
            temp=0
            for i in range(M):
                temp+=data[y-i][x-i]
                temp+=data[y][x-i]
                temp+=data[y-i][x]
                s=data[i]
            if temp>ans:
                ans=temp

    print(ans)