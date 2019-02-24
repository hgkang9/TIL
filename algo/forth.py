import sys
sys.stdin = open("forth.txt", "r")

T = int(input())

for tc in range(1, T+1):
    stack = []
    data = list(map(str, input().split()))
    for i in range(len(data)):
        if data[i] != '+' and data[i] != '-' and data[i] != '*' and data[i] != '/' and data[i] != '.':
            stack.append(data[i])
        elif len(stack)>=2 and data[i] == '+':
            res = int(stack[-1]) + int(stack[-2])
            stack.pop(-1)
            stack.pop(-1)
            stack.append(int(res))
        elif len(stack)>=2 and data[i] == '-':
            res = int(stack[-2]) - int(stack[-1])
            stack.pop(-1)
            stack.pop(-1)
            stack.append(int(res))
        elif len(stack)>=2 and data[i] == '*':
            res = int(stack[-1]) * int(stack[-2])
            stack.pop(-1)
            stack.pop(-1)
            stack.append(int(res))
        elif len(stack)>=2 and data[i] == '/':
            res = int(stack[-2]) / int(stack[-1])
            stack.pop(-1)
            stack.pop(-1)
            stack.append(int(res))
        elif len(stack)==1 and data[i] == '.':
            print(f'#{tc} {stack[-1]}')
            break
        else:
            print(f'#{tc} error')
            break