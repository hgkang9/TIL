import sys
sys.stdin = open("이진힙.txt", "r")

T=int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [0]+list(map(int, input().split()))
    res = 0

    # Heap=[0]*(N+1)
    # for here in range(1, N+1):
    #     Heap[here] = data[here]
    #     pa = here//2
    #     while pa:
    #         if data[pa] > data[here]:
    #            data[here], data[pa] = data[pa], data[here]
    #         else:
    #             break
    #         here = pa
    #         pa = here//2

    for here in range(1, N+1):
        pa = here//2
        while pa:
            if data[pa] > data[here]:
                data[here], data[pa] = data[pa], data[here]
            else:
                break
            here = pa
            pa = here//2

    while N>=1:
        res += data[N//2]
        N = N//2
    print('#%d %d' %(tc, res))
    print('#{} {}' .format(tc, res))