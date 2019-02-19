import sys
sys.stdin = open("screw.txt", "r")

# TC = int(input())
# for tc in range(1, TC+1):
#     n = int(input())
#     data = list(map(int, input().split()))
#
#     for i in range(0, n*2-3, 2):
#         if data[i] == data[i+3]:
#             data[i], data[i+2] = data[i+2], data[i]
#             data[i+1], data[i+3] = data[i+3], data[i+1]
#         else:
#             pass
#
#     print(f'#{tc}', end=" ")
#
#     for i in data:
#         print(i, end=" ")
#
#     print()


n = 6
data = [1,2,2,3,8,1,3,7,5,8,9,5]

for i in range(0, n*2-3, 2):
    if data[i] == data[i+3]:
        data[i], data[i+2] = data[i+2], data[i]
        data[i+1], data[i+3] = data[i+3], data[i+1]


for i in data:
    print(i, end=" ")