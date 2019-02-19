import sys
sys.stdin = open("specialsort.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    data = list(map(int, input().split()))
    ans = []
    data.sort()
    count = 0

    for i in range(10):
        if count % 2:
            ans.append(data.pop(0))
            count += 1
        else:
            ans.append(data.pop(-1))
            count += 1


    print(f'#{tc}', end=" ")

    for i in ans:
        print(i, end=" ")

    print()




