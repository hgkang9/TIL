import sys
sys.stdin = open('view.txt', 'r')

def getmax(here):
    mymax = heights[here-2]
    if mymax < heights[here-1]:
        mymax = heights[here-1]
    if mymax < heights[here+1]:
        mymax = heights[here+1]
    if mymax < heights[here+2]:
        mymax = heights[here+2]

    return mymax

TC = 10
for tc in range(1, TC+1):
    N = int(input())
    heights = list(map(int, input().split()))

    ans = 0

    for here in range(2, N-2):
        side = getmax(here)
        if side < heights[here]:
            ans += heights[here] - side

    print('#%d %d' %(tc, ans))