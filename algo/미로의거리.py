import sys
sys.stdin = open("미로.txt", "r")

TC = int(input())

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def ispossible(y, x):
    global N
    if y >= 0 and y < N and x >= 0 and x < N and not visited[y][x]:

        return True

def bfs(y, x):
    global ans, count
    que.append((y, x))
    visited[y][x] = 1

    while que:
        (y, x) = que.pop(0)
        # if data[y][x] == 3:
        #     ans = 1
        #     return

        for dir in range(4):
            newy = y + dy[dir]
            newx = x + dx[dir]
            if ispossible(newy, newx):
                if data[newy][newx] == 0:
                    visited[newy][newx] = 1 # 지나왔던 길을 알려주기 위해서
                    distance[newy][newx] = distance[y][x]+1
                    que.append((newy, newx))
                elif data[newy][newx] == 3:
                    ans = 1
                    return distance[y][x]

for tc in range(1, TC + 1):
    start_x = 0
    start_y = 0
    N = int(input())
    visited = [[0 for _ in range(N)] for _ in range(N)]
    distance = [[0 for _ in range(N)] for _ in range(N)]
    que = []
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input()))

    for y in range(N):
        for x in range(N):
            if data[y][x] == 2:
                start_x = x
                start_y = y
                break
    ans = 0

    # bfs(start_y, start_x)
    if ans == 1:
        print(f'#{tc} {bfs(start_y, start_x)}')
    else:
        print(f'#{tc} {ans}')