def sel(data, i):
    if i==len(data)-1:
        return

    # for j in range(i+1,len(data)):
    #     if data[i]>data[j]:
    #         data[i], data[j] = data[j], data[i]

    min=i
    for j in range(i+1, len(data)):
        if data[min]>data[j]:
            min=j
    data[min],data[i]=data[i],data[min]
    sel(data, i+1)

# data=[34,10,16,89,54,23,67]
data=[599,654,1,561,8,246,686,51,684,65,16,87,62,5,98,32]
sel(data,0)
print(data)