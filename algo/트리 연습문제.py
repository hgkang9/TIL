# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
import sys
sys.stdin = open("트리연습.txt", "r")
node = int(input())
tree = [[0 for _ in range(5)] for _ in range(node+1)]
data=list(map(int, input().split()))
for i in range(node-1):
    pa, ch = data[i*2], data[i*2+1]
    if tree[pa][0] == 0:
        tree[pa][0] = ch
        tree[pa][2] += 1
        tree[ch][3] = pa
        tree[ch][4] = tree[pa][4] + 1
    else:
        tree[pa][1] = ch
        tree[pa][2] += 1
        tree[ch][3] = pa
        tree[ch][4] = tree[pa][4] + 1
print(tree)
