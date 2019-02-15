import sys
sys.stdin = open('flatten.txt', 'r')

T = 10

for tc in range(1, T+1):
    C = int(input())
    data = list(map(int, input().split()))

    max = data[0]
    maxindex = 0
    min = data[0]
    minindex = 0
    count = 0
    ans = 0

    for i in range(len(data)):
        if data[i] > max:
            max = data[i]
            maxindex = i

    for i in range(len(data)):
        if data[i] < min:
            min = data[i]
            minindex = i

    while count <= C:
        data[maxindex] -= 1
        data[minindex] += 1
        count += 1
        ans = data[maxindex] - data[minindex]
        if ans == 0 or 1:
            break

    print('#%d %d' %(tc, ans))