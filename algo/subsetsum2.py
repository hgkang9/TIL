import sys
sys.stdin = open("subsetsum2.txt", "r")

TC = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
l = len(A)

for tc in range(1, TC+1):
    N, K = map(int, input().split())
    count = 0

    for i in range(1 << l):
        subset = []
        for j in range(l):
            if i & (1 << j):
                subset.append(A[j])
        if len(subset) == N:
            if sum(subset) == K:
                count += 1
    print('#%d %d' %(tc, count))