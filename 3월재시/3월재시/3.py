import sys
sys.stdin=open('금속막대기.txt','r')


def GetSome(k,sum):
    global flag
    if sum==L:
        flag=1
        return
    if k>=N or sum>L:
        return
    visited[k]=True
    GetSome(k+1,Stick[k]+sum)
    visited[k]=False
    GetSome(k+1,sum)



TC=int(input())
for tc in range(1,TC+1):
    print("#%d"%tc,end=' ')
    N,L=map(int,input().split())
    Stick=list(map(int,input().split()))
    visited=[0]*N
    flag=0
    GetSome(0,0)
    print(flag)




















