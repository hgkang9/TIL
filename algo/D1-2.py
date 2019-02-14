import sys

sys.stdin = open('input2.txt', 'r') # 파일에서 읽을 때 사용

data = list(map(int, input().split()))

max = data[0] # 가장 안전한 방법/첫 값을 기준
count = 0
count_re = 0

while count_re < len(data):
    for i in data:
        if max > i :
            count += 1
            count_re += 1
        else:
            max = i
            count_re += 1

print(count)

#강사님
high = 0

for now in range(len(data)):
    cnt = len(data)-now-1
    for next in range(now+1, len(data)):
        if data[next] >= data[now]:
            cnt -= 1
    if cnt > high:
        high = cnt

print(high)
