arr = [-3,3,-9,6,7,-6,1,5,4,-2]

n = len(arr)

for i in range(1<<n):
    subset = []
    for j in range(n):
        if i & (1<<j):
            subset.append(arr[j])
    # print(sum(subset))
    if sum(subset) == 0:
        print(subset)
