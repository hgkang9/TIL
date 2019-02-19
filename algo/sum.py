import sys
sys.stdin = open("sum.txt", "r")

data = [[0 for _ in range(100)] for _ in range(100)]

def row_sum(a):
    sum1=0
    for i in a:
        sum1 += i
    return sum1


TC = 10
for tc in range(1, TC+1):
    N = int(input())
    for i in range(100):
        data[i] = list(map(int, input().split()))












    print('#%d %d' % (tc, ans))