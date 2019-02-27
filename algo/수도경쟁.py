import sys
sys.stdin = open("수도경쟁.txt", "r")

TC = int(input())

for tc in range(1,TC+1):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    if W <= R:
        B = Q
    else:
        B = Q + (S * (W - R))

    if A < B:
        print(f'#{tc} {A}')
    else:
        print(f'#{tc} {B}')