import sys
sys.stdin = open('농작물.txt','r')
TC=int(input())
for tc in range(1,TC+1):
    N=int(input())
    m=(N//2)
    sum=0
    data=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input()))

    for y in range(N):
        sum += data[y][m]
        if y<=m and y>=1:
            for i in range(1, y+1):
                sum += data[y][m-i]
                sum += data[y][m+i]
        elif y>m and y<N:
            for i in range(1,(y-2*(y-m))+1):
                sum += data[y][m - i]
                sum += data[y][m + i]
    print('#%d %d' %(tc,sum))