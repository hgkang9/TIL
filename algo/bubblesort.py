import sys

sys.stdin = open('input3.txt', 'r') # 파일에서 읽을 때 사용

data = list(map(int, input().split()))

all = len(data)
for now in range(all-1):
    for next in range(now+1, all):
        if data[next] < data[now]:
            data[now], data[next] = data[next], data[now]

print(data)