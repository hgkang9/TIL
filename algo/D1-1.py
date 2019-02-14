import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

data = list(map(int, input().split()))

max = data[0] # 가장 안전한 방법/첫 값을 기준
count = -1

for i in data:
    count += 1
    if max < i:
        max = i
        maxindex = count
    else:
        pass

print(max, maxindex+1)

# min = data[0] # 987654321, 0x7FFFFFFF 가능