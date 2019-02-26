import sys
sys.stdin = open("회전.txt", "r")

TC = int(input())

for tc in range(1,TC+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    O = M % N

    for i in range(O):
        out = data.pop(0)
        data.append(out)

    print(f'#{tc} {data[0]}')
