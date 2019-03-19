import sys
sys.stdin=open('암호코드스캔.txt','r')
T = int(input())
password = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
            '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(str, input()))
    passdata = [0] * 56
    realfake = [0] * 8
    p = 55
    for y in range(N):
        for x in range(M):
            if data[y][x]=="A":
                data[y][x]='10'
            elif data[y][x]=="B":
                data[y][x]='11'
            elif data[y][x]=="C":
                data[y][x]='12'
            elif data[y][x]=="D":
                data[y][x]='13'
            elif data[y][x]=="E":
                data[y][x]='14'
            elif data[y][x]=="F":
                data[y][x]='15'
    for i in range(N):
        data=list(map(int,data))
    print(data)
    list(input() for _ in range)]
    # for y in range(N):
    #     for x in range(M - 1, -1, -1):
    #         if data[y][x]:
    #             while p:
    #                 passdata[p] = data[y][x]
    #                 p -= 1
    #                 x -= 1
    #             break
    #
    # passdata = list(map(str, passdata))
    #
    # lp = len(passdata)
    # t = 0
    # for j in range(lp - 6):
    #     b = ''.join(passdata[j:j + 7])
    #     if b in password:
    #         realfake[t] = password[b]
    #         passdata[j:j + 7] = ['5', '5', '5', '5', '5', '5', '5']
    #         t += 1
    #
    # sum = 0
    # ans = 0
    # for i in range(8):
    #     if i % 2:
    #         sum += realfake[i]
    #     else:
    #         sum += (3 * realfake[i])
    #
    # if sum % 10:
    #     print('#%d 0' % tc)
    # else:
    #     for i in range(8):
    #         ans += realfake[i]
    #     print('#{} {}'.format(tc, ans))
