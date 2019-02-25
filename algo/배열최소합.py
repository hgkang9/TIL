import sys
sys.stdin = open("배열최소합.txt", "r")

T = int(input())

def minsum(y):
    global ans, N, msum
    if y == N:
        if ans < msum:
            msum = ans
            return

    if ans >= msum:
        return

    for x in range(N):
        if not visitedx[x]:
            visitedx[x] = True
            ans += data[y][x]
            minsum(y + 1)
            visitedx[x] = False

for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    ans = 0
    visitedx = [0]*N

    msum = 987654321

    minsum(0)

    print(msum)


