import sys
sys.stdin = open("ladder.txt", "r")

TC = 10
data = [[0 for _ in range(100)] for _ in range(100)]

for tc in range(1, TC+1):
    here_x = 0
    here_y = 0
    end_y = 99
    N = int(input())
    for i in range(100):
        data[i] = list(map(int, input().split()))

    for x in range(100):
        if data[end_y][x] == 2:
            here_x = x
            here_y = end_y
            break

    # for i in range(999):
    while True:
        if here_x-1 >= 0 and data[here_y][here_x-1] == 1:
            here_x = here_x-1
            data[here_y][here_x+1] = 2

        elif here_x+1 < 100 and data[here_y][here_x+1] == 1:
            here_x = here_x+1
            data[here_y][here_x-1] = 2

        elif here_y == 0:
            print(f'#{tc} {here_x}')
            break
        else:
            here_y = here_y - 1