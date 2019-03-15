data=[38,27,43,3,9,82,10]
def merge(left, right):
    l=len(left)+len(right)
    res=[0]*l
    i, j, k = 0, 0, 0
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

ans=mergesort(data)

print(ans)

