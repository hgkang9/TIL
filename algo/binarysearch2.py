import sys
sys.stdin = open("binarysearch2.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    P, Pa, Pb = map(int, input().split())

    start = 1
    end = P
    mid = (start + end) // 2
    count_Pa = 1
    count_Pb = 1
    winner = ''

    for i in range(1, P+1):

        if Pa < mid:
            end = mid
            mid = (start + end) // 2
            count_Pa += 1
        elif Pa > mid:
            start = mid
            mid = (start + end) // 2
            count_Pa += 1
        else:
            break

    start = 1
    end = P
    mid = (start + end) // 2

    for i in range(1, P+1):

        if Pb < mid:
            end = mid
            mid = (start + end) // 2
            count_Pb += 1
        elif Pb > mid:
            start = mid
            mid = (start + end) // 2
            count_Pb += 1
        else:
            break

    if count_Pa < count_Pb:
        winner = 'A'
    elif count_Pa > count_Pb:
        winner = 'B'
    else:
        winner = 0

    print(f'#{tc} {winner}')