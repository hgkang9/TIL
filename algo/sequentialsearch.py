arr = [2,4,11,7,19,9,23]
arr.sort()

search = 11

l = len(arr)

for i in range(l):
    if arr[i] == search:
        print("성공")
        print(f'{i+1}번째')

    if search not in arr:
        print("없음")
        break
