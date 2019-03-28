from collections import deque
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    visited=[0]*1000001
    que=deque()
    que.append((0,N))
    i,j=0,0
    while que:
        i=que[0][0]
        i+=1
        j=que[0][1]*2
        if j<=1000000 and not visited[j]:
            visited[j]=1
            que.append((i,j))
            if j==M:
                break

        j = que[0][1]+1
        if j <= 1000000 and not visited[j]:
            visited[j] = 1
            que.append((i, j))
            if j==M:
                break

        j = que[0][1]-1
        if j <= 1000000 and not visited[j]:
            visited[j] = 1
            que.append((i, j))
            if j==M:
                break

        j = que[0][1]-10
        if j <= 1000000 and not visited[j]:
            visited[j] = 1
            que.append((i, j))
            if j==M:
                break

        que.popleft()

    print('#%d %d' %(tc,que[-1][0]))

