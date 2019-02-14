import sys

sys.stdin = open('babygin.txt', 'r') # 파일에서 읽을 때 사용

data = list(map(int, input().split()))

counts = [0] * 10

for i in data:
    counts[i] += 1

for j in range(len(counts)):
    if counts[j] >= 3:
        counts[j] = counts[j]-3

    if counts[j]:
        if counts[j+1]:
            if counts[j+2]:

                print('babygin')