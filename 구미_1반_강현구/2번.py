import sys
sys.stdin=open('2번.txt','r')

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    data=[list(map(int,input().split())) for i in range(N)]

    low = -1
    for y in range(1, N):
        for x in range(1, M):
            A = 0
            B = 0
            C = 0
            D = 0

            for i in range(y):
                for a in range(x):
                    A += data[i][a]
                for b in range(x, M):
                    B += data[i][b]

            for i in range(y, N):
                for d in range(x):
                    C += data[i][d]
                for e in range(x, M):
                    D += data[i][e]

            li = [A, B, C, D]

            for i in range(4):
                for j in range(i+1,4):
                    k = li[i]
                    l = li[j]
                    ans = abs(k-l)
                    if ans>low:
                        low = ans

    print('#%d %d' %(tc,low))