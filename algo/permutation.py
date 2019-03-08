import sys

sys.stdin = open('input3.txt', 'r') # 파일에서 읽을 때 사용

data = list(map(int, input().split()))
cand1 = 0

for i in range(len(data)-1):
    if data[i] <= data[i+1]:
        cand1 = i

if cand1 != 0:

    data[cand1+1:] = data[:cand1:-1]

    # cand2 = len(data) -1
    # while data[cand1] > data[cand2]:
    #     cand2 -= 1

    for cand2 in range(cand1+1, len(data)):
        if data[cand2] > data[cand1]:
            break

    data[cand1], data[cand2] = data[cand2], data[cand1]

    print(data)