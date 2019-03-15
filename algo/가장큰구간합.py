data=[5,1,-4,2,-1,-5,-2,8,-3,6]
rangesum=[0]*len(data)
rangesum[0]=data[0]

for i in range(1,len(data)):
    rangesum[i]=max(rangesum[i-1]+data[i], data[i])

print(max(rangesum))

