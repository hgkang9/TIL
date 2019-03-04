import sys
sys.stdin = open("문자열비교kmp.txt", "r")

TC = int(input())

for tc in range(1,TC+1):
    pattern = list(map(str, input()))
    stringgg = list(map(str, input()))
    pitable = [0] * len(pattern)
    pitable[0] = -1
    i, j = 0, 1

    for i in range(len(pattern)-2):
        if pattern[i] == pattern[j]:
            pitable[j+1] = pitable[j] + 1
            i += 1
            j += 1
        else:
            i = 0
            if pattern[i] == pattern[j]:
                pitable[j+1] = 1
                j += 1
            else:
                pitable[j+1] = 0
                j += 1

    isfind = False
    p = 0
    q = 0
    count = 0
    temp = 0

    while p <= len(stringgg)-1:
        if stringgg[p] == pattern[q]:
            count += 1
            p += 1
            q += 1
        else:
            p = temp + count - pitable[count]
            temp = p
            q = 0
            count = 0
        if count == len(pattern):
            isfind = True
            break

    if isfind == True:
        print('#%d' %tc, end=' ')
        print(1)
    else:
        print('#%d' %tc, end=' ')
        print(0)