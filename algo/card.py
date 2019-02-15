import sys
sys.stdin = open('card.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input()))

    count = [0] * 10

    for i in data:
        count[i] += 1

    ans = count[0]

    for i in range(len(count)):
        if count[i] >= ans:
            ans = count[i]
            ansindex = i

    print('#%d %d %d' %(tc, ansindex, ans))