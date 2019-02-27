import sys
sys.stdin = open("노드의거리.txt", "r")

TC = int(input())

def bfs(S):
    global V, G, ans
    que.append(S)
    visited[S] = 1

    while que:
        S = que.pop(0)
        if S == G:
            ans=1
            return distance[G]

        for next in range(V+1):
            if mymap[S][next] and not visited[next]:
                que.append(next)
                distance[next]=distance[S]+1
                visited[next]=1


for tc in range(1, TC + 1):
    V, E = map(int, input().split())
    route = []
    for i in range(E):
        route += list(map(int, input().split()))
    S, G = map(int, input().split())
    mymap = [[0] * (V + 1) for i in range(V + 1)]
    visited = [0] * (V + 1)
    distance = [0] * (V + 1)
    que=[]

    for i in range(int(E)):
        start = route[i * 2]
        stop = route[i * 2 + 1]
        mymap[start][stop] = 1
        mymap[stop][start] = 1

    ans = 0
    res = bfs(S)

    if ans == 1:
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} {ans}')