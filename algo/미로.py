import sys
sys.stdin = open("미로.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    here_x = 0
    here_y = 0
    start_x = 0
    start_y = 0
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input()))

    for y in range(N):
        for x in range(N):
            if data[y][x] == 2:
                here_x = x
                here_y = y
                start_x = x
                start_y = y
                break

    # for i in range(999):
    while True:
        if here_x-1 >= 0 and data[here_y][here_x-1] == 0:
            here_x = here_x-1
            data[here_y][here_x+1] = 5

        elif here_x+1 < N and data[here_y][here_x+1] == 0:
            here_x = here_x+1
            data[here_y][here_x-1] = 5

        elif here_y - 1 >= 0 and data[here_y-1][here_x] == 0:
            here_y = here_y - 1
            data[here_y+1][here_x] = 5

        elif here_y+1 < N and data[here_y+1][here_x] == 0:
            here_y = here_y+1
            data[here_y-1][here_x] = 5

        elif (data[here_y][here_x - 1] != 3 and data[here_y][here_x + 1] != 3 \
                 and data[here_y - 1][here_x] != 3 and data[here_y + 1][here_x] != 3):

            if data[start_y][start_x - 1] != 0 and data[start_y][start_x + 1] != 0 \
                and data[start_y - 1][start_x] != 0 and data[start_y + 1][start_x] != 0:
                print(f'#{tc} 0')
                break
            else:
                here_x = start_x
                here_y = start_y

        elif (data[here_y][here_x-1] == 3 or data[here_y][here_x+1] == 3 \
                or data[here_y-1][here_x] == 3 or data[here_y+1][here_x] == 3):
            print(f'#{tc} 1')
            break