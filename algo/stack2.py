import sys
sys.stdin = open("stack2.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    data = input()
    stack = [0]
    l = len(data)
    for i in range(l):
        if data[i] != '(' and data[i] != ')' and data[i] != '{' and data[i] != '}':
            pass

        elif data[i] == '(' or data[i] == '{':
            stack.append(data[i])

        elif data[i] == ')' or data[i] == '}':
            if (data[i] == ')' and stack[-1] == '{') or (data[i] == '}' and stack[-1] == '('):
                break

            elif (data[i] == ')' and stack[-1] == '(') or (data[i] == '}' and stack[-1] == '{'):
                stack.pop(-1)

            elif stack[-1] == 0:
                stack.append(99)

    if stack[-1] == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
