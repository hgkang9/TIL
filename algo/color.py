import sys
sys.stdin = open("color.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    background = [[0 for _ in range(10)] for _ in range(10)]
    data = []
    count = 0
    for i in range(N):
        data.append(list(map(int, input().split())))

    for i in range(N):
        for y in range(data[i][0], data[i][2]+1):
            for x in range(data[i][1], data[i][3]+1):
                background[y][x] += 1

    for y in range(10):
        for x in range(10):
            if background[y][x] == 2:
                count += 1

    print('#%d %d' %(tc, count))
