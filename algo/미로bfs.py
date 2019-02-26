import sys
sys.stdin = open("미로.txt", "r")

TC = int(input())

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def ispossible(y, x):
    global N
    if y >= 0 and y < N and x >= 0 and x < N and not visited[y][x]:
        if (data[y][x] == 0 or data[y][x] == 3):
            return True

def bfs(y, x):
    que.append((y, x))
    visited[y][x] = 1
    global ans

    while que:
        (y, x) = que.pop(0)
        if data[y][x] == 3:
            ans = 1
            return

        for dir in range(4):
            newy = y + dy[dir]
            newx = x + dx[dir]
            if ispossible(newy, newx):
                visited[newy][newx] = 1 # 지나왔던 길을 알려주기 위해서
                que.append((newy, newx))


for tc in range(1, TC + 1):
    start_x = 0
    start_y = 0
    N = int(input())
    visited = [[0 for _ in range(N)] for _ in range(N)]
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

    bfs(start_y, start_x)

    print(f'#{tc} {ans}')