arr = [2,3,4,1,5,7,6]
arr.sort()

search = 4

n = len(arr)
start = 0
end = n-1
mid = (start + end) // 2

for i in range(n):
    if search < arr[mid]:
        end = mid-1
        mid = (start + end) // 2
        if end == 0:
            print("없음")
            break
    elif search == arr[mid]:
        print("성공")
        break
    elif search not in arr:
        print("없음")
        break
    else:
        start = mid+1
        mid = (start+end) // 2

print(arr[mid])