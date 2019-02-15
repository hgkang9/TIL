import sys
sys.stdin = open('4835.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    partmax = 0
    partmin = 987654321

    for i in range(len(data)-(M-1)):
        count1 = 1
        temp1 = data[i]
        while count1 < M:
            temp1 += data[i+1]
            count1 += 1
            i += 1
            sum1 = temp1

        if sum1 > partmax:
            partmax = sum1


    for i in range(len(data)-(M-1)):
        count2 = 1
        temp2 = data[i]
        while count2 < M:
            temp2 += data[i + 1]
            count2 += 1
            i += 1
            sum2 = temp2

        if sum2 < partmin:
            partmin = sum2

    ans = partmax - partmin

    print('#%d %d' %(tc, ans))
