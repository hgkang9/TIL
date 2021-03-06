import sys

sys.stdin = open('input4.txt', 'r') # 파일에서 읽을 때 사용

data = list(map(int, input().split()))

counts = [0] * 5
temps = [0] * 8

for i in data:
    counts[i] += 1

for j in range(1, len(counts)):
    counts[j] = counts[j] + counts[j-1]

for k in data:
    counts[k] -= 1
    temps[counts[k]] = k

print(temps)

# 강사님
howmany = len(data)

count = [0] * 5
result = [0] * howmany

for i in range(howmany):
    count[data[i]] += 1

for i in range(1, len(count)):
    count[i] += count[i-1]

for i in range(len(data)-1, -1, -1):
    count[data[i]] -= 1
    result[count[data[i]]] = data[i]

print(result)