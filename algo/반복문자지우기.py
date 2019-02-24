import sys
sys.stdin = open("반복문자지우기.txt", "r")

TC = int(input())
data = []
l = len(data)

# def delete(data):
#     for i in range(l):
#         if data[i] == data[i+1]:
#             data.pop(i)
#             data.pop(i+1)
#             delete(data)
#         else:
#             return

for tc in range(1, TC+1):
    data = list(map(str, input()))
    l = len(data)
    # delete(data)
    for i in range(l):
        if data[i] == data[i+1]:
            data[i] = 0
            data[i+1] = 0

    print(f'#{tc} {len(data)}')
