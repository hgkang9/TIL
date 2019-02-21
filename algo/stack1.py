stack = [0] * 100
top = -1

# for i in range(1,4):
#     stack.append(i)
#
# while stack:
#     print(stack.pop())
#
# for i in range(1,4):
#     top += 1
#     stack[top] = i
#
# # for i in range(3):
# while top != -1:
#     print(stack[top])
#     top -= 1

data = '()()))'
l = len(data)
info = [0] * 128
info[ord(')')] = '('
info[ord('}')] = '{'
info[ord(']')] = '['
info[ord('>')] = '<'

for i in range(l):
    if data[i] == '('or data[i] == '{' or data[i] == '[' or data[i] == '<':
        top += 1
        stack[top] = data[i]
    elif info[ord(data[i])] == stack[top]:
        top -= 1
    else:
        top = 9999999
        break

if top == -1:
    print('right')
else:
    print('wrong')

