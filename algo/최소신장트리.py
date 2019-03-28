import sys
sys.stdin=open('최소신장트리.txt','r')
T=int(input())
for tc in range(1,T+1):
    V,E=map(int,input().split())
    data=[0]*E
    for i in range(E):
        data[i]=tuple(map(int,input().split()))
    data.sort(key=lambda x:x[2])
    visited=[0]*(V+1)
    cnt,ans,p=0,0,0
    # while True:
    #     visited[p]=1
    #     for i in range()
    #     if path[

    print(data)
