import sys

sys.stdin = open("미로.txt", "r")

TC = int(input())

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def ispossible(y, x):
    global N
    if y >= 0 and y < N and x >= 0 and x < N:
        if (data[y][x] == 0 or data[y][x] == 3):
            return True

def go(y, x):
    global ans
    if data[y][x] == 3:
        ans = 1
        return

    for dir in range(4):
        newy = y + dy[dir]
        newx = x + dx[dir]
        if ispossible(newy, newx):
            data[y][x] = 5  # 지나왔던 길을 알려주기 위해서
            go(newy, newx)

for tc in range(1, TC + 1):
    start_x = 0
    start_y = 0
    N = int(input())
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

    go(start_y, start_x)

    print(f'#{tc} {ans}')