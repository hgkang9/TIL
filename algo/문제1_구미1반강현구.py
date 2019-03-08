import sys
sys.stdin=open('문제1.txt','r')
T=int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    a=K//2
    b=a-1
    sum_left=0
    sum_right=0
    ans=987654321
    temp=0
    if K%2: # X의 크기가 홀수인 경우
        for y in range(a, N-a):
            for x in range(a, N-a):
                sum_left=0
                sum_right=0
                for i in range(1,a+1):
                    sum_right+=data[y][x]
                    sum_right+=data[y-i][x-i]
                    sum_right+=data[y+i][x+i]
                    sum_left+=data[y][x]
                    sum_left+=data[y-i][x+i]
                    sum_left+=data[y+i][x-i]
                    temp=abs(sum_right-sum_left)
                if temp<ans:
                    ans=temp
    else: # X의 크기가 짝수인 경우
        for y in range(a, N-b):
            for x in range(a, N-b):
                sum_left=0
                sum_right=0
                for i in range(1,a+1):
                    sum_right+=data[y-i][x-i]
                    sum_right+=data[y+(i-1)][x+(i-1)]
                for i in range(1,a+1):
                    sum_left+=data[y-i][x+(i-1)]
                    sum_left+=data[y+(i-1)][x-i]
                temp=abs(sum_right-sum_left)
                if temp<ans:
                    ans=temp
    print('#%d %d' %(tc, ans))