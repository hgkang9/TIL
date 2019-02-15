import sys
sys.stdin = open('minmax.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    max = ai[0]
    min = ai[0]

    for i in ai:
        if i > max:
            max = i

    for i in ai:
        if i < min:
            min = i

    ans = max - min

    print('#%d %d' %(tc, ans))