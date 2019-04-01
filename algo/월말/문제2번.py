import sys
sys.stdin=open('문제2.txt','r')

#임의의 세 구역 절대값 계산
def calc(a,b,c):
    global cs
    cs=0
    cs=abs(a-b)+abs(b-c)+abs(c-a)
    return cs

#한 구역의 합 계산
def psum(y1,y2,x1,x2):
    global res
    res=0
    for y in range(y1,y2):
        for x in range(x1,x2):
            res+=data[y][x]
    return res

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    data=[list(map(int,input().split())) for _ in range(N)]
    res,ans,cs=0,0,0
    for y in range(1,N):
        for x1 in range(1,M-2):
            for x2 in range(2,M-1):
                sum1 = psum(0, y, 0, x1)
                sum2 = psum(0, y, x1, x2)
                sum3 = psum(0, y, x2, M)
                sum4 = psum(y, N, 0, x1)
                sum5 = psum(y, N, x1, x2)
                sum6 = psum(y, N, x2, M)
                data1 = [(sum1, sum2, sum3), (sum1, sum2, sum4), (sum1, sum2, sum5), (sum1, sum2, sum6),
                         (sum1, sum3, sum4), (sum1, sum3, sum5), (sum1, sum3, sum6),
                         (sum1, sum4, sum5), (sum1, sum4, sum6), (sum1, sum5, sum6),
                         (sum2, sum3, sum4), (sum2, sum3, sum5), (sum2, sum3, sum6),
                         (sum2, sum4, sum5), (sum2, sum4, sum6), (sum2, sum5, sum6),
                         (sum3, sum4, sum5), (sum3, sum4, sum6), (sum3, sum5, sum6),
                         (sum4, sum5, sum6)]
                for i in range(len(data1)):
                    calc(data1[i][0],data1[i][1],data1[i][2])
                    if cs>ans:
                        ans=cs

    print('#%d %d' %(tc,ans))

