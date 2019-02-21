import sys
sys.stdin = open("graph2.txt", "r")

TC = int(input())
V, E = 0, 0
route = []
visited = []
ans = 0

def dfs(here, last):
    if here==last :
        visited[here] = True
        ans = 1
    for i in range(V+1):
        if mymap[here][i] and not visited[i]:
            visited[i] = True
            dfs(i, last)

for tc in range(1,TC+1):
    V, E = map(int, input().split())
    route = []
    for i in range(E):
        route += list(map(int, input().split()))
    S, G = map(int, input().split())
    mymap = [[0] * (V+1) for i in range(V+1)]
    visited = [0] * (V+1)

    for i in range(int(E)):
        start = route[i*2]
        stop = route[i*2+1]
        mymap[start][stop] = 1

    dfs(S, G)

    if visited[G]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')