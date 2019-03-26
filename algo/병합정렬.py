import sys
sys.stdin=open('병합정렬.txt','r')

def merge(left, right):
    global cnt
    l=len(left)+len(right)
    res=[0]*l
    i, j, k = 0, 0, 0
    if left and right:
        if left[-1] > right[-1]:
            cnt += 1
    while left or right:
        if not left:
            res[k]=right.pop(j)
            k+=1
            if not right:
                return res
        elif not right:
            res[k]=left.pop(i)
            k+=1
            if not left:
                return res
        elif left[i]>=right[j]:
            res[k]=right.pop(j)
            k+=1
        else:
            res[k]=left.pop(i)
            k+=1

def mergesort(data):
    if len(data)<=1:
        return data
    left=mergesort(data[:len(data)//2])
    right=mergesort(data[len(data)//2:])
    return merge(left, right)

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    data=list(map(int,input().split()))
    cnt=0
    ans=mergesort(data)
    print('#%d %d %d' %(tc, ans[N//2], cnt))