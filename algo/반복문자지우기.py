import sys
sys.stdin = open("반복문자지우기.txt", "r")

TC = int(input())
data = []

def delete(data):
    for i in range(len(data)):
        if data[i] == data[i+1]:
            data.pop(i)
            data.pop(i+1)
            delete(i-2)

for tc in (1, TC+1):
    data = list(map(str, input()))
    delete(data)
    print(f'#{tc} {len(data)}')
