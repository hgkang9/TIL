import sys
sys.stdin = open("회문.txt", "r")

TC = int(input())

def garo(a):
    global M
    for i in range(M):
        temp1.append(a[i])
        temp2.append(a[i])
        temp1.reverse()
        if temp1 == temp2:
            return temp1


for tc in range(1,TC+1):
    N, M = map(int, input().split())
    pan = [[0 for _ in range(N)] for _ in range(N)]
    temp1 = []
    temp2 = []
    temp3 = []

    for i in range(N):
        pan[i] = list(map(str, input()))

    for y in range(N):
        if garo(pan[y]):
            print(temp1)

    # for x in range(N):
    #     for y in range(N):
    #
    #     temp3.append(pan[y][x])
    # print(garo)


